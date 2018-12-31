if (typeof jQuery === 'undefined') {
    var jQuery = django.jQuery;
}

(function ($) {
    $(function () {
        $('.mediasortedm2m-container').find('.mediasortedm2m-items').addClass('hide');
        function prepareUl(ul) {
            ul.addClass('mediasortedm2m');
            var checkboxes = ul.find('input[type=checkbox]');
            var id;
            var name;

            if (checkboxes.length) {
                id = checkboxes.first().attr('id').match(/^(.*)_\d+$/)[1];
                name = checkboxes.first().attr('name');
                checkboxes.removeAttr('name');
            } else {
                var label;
                var currentElement = ul;

                while (!label || !label.length) {
                    currentElement = currentElement.parent();
                    label = currentElement.siblings('label');
                }

                id = label.attr('for').match(/^(.*)_\d+$/)[1];
                name = id.replace(/^id_/, '');
            }

            ul.before('<input type="hidden" id="' + id + '" name="' + name + '" />');
            var recalculate_value = function () {
                var values = [];
                ul.find(':checked').each(function () {
                    values.push($(this).val());
                });
                $('#' + id).val(values.join(','));
            };
            recalculate_value();
            ul.on('change','input[type=checkbox]',recalculate_value);
            ul.sortable({
                axis: 'y',
                //containment: 'parent',
                update: recalculate_value
            });
            return ul;
        }

        function iterateUl() {
            $('.mediasortedm2m-items').each(function () {
                var ul = $(this);

                prepareUl(ul);
                ul.removeClass('hide');
            });
        }

        $(".add-row a").click(iterateUl);

        iterateUl();

        $('.mediasortedm2m-container .selector-filter input').each(function () {
            $(this).bind('input', function() {
                var search = $(this).val().toLowerCase();
                var $el = $(this).closest('.selector-filter');
                var $container = $el.siblings('.mediasortedm2m-items').each(function() {
                    // walk over each child list el and do name comparisons
                    $(this).children().each(function() {
                        var curr = $(this).find('label').text().toLowerCase();
                        if (curr.indexOf(search) === -1) {
                            $(this).css('display', 'none');
                        } else {
                            $(this).css('display', 'inherit');
                        }
                    });
                });
            });
        });

        var dismissPopupFnName = 'dismissAddAnotherPopup';
        // django 1.8+
        if (window.dismissAddRelatedObjectPopup) {
            dismissPopupFnName = 'dismissAddRelatedObjectPopup';
        }

        function html_unescape(text) {
            // Unescape a string that was escaped using django.utils.html.escape.
            text = text.toString().replace(/&lt;/g, '<');
            text = text.toString().replace(/&gt;/g, '>');
            text = text.toString().replace(/&quot;/g, '"');
            text = text.toString().replace(/&#39;/g, "'");
            text = text.toString().replace(/&amp;/g, '&');
            return text;
        }

        if (window.showAddAnotherPopup) {
            var django_dismissAddAnotherPopup = window[dismissPopupFnName];
            window[dismissPopupFnName] = function (win, newId, newRepr) {
                // newId and newRepr are expected to have previously been escaped by
                // django.utils.html.escape.
                newRepr = JSON.parse(newRepr);
                newId = html_unescape('' + newId);
                var name = windowname_to_id(win.name);
                var elem = $('#' + name);
                var mediasortedm2m = elem.siblings('.mediasortedm2m-items.mediasortedm2m');
                if (mediasortedm2m.length == 0) {
                    // no mediasortedm2m widget, fall back to django's default
                    // behaviour
                    return django_dismissAddAnotherPopup.apply(this, arguments);
                }

                if (elem.val().length > 0) {
                    elem.val(elem.val() + ',');
                }
                elem.val(elem.val() + newId);

                var id_template = '';
                var maxid = 0;
                mediasortedm2m.find('.mediasortedm2m-item input').each(function () {
                    var match = this.id.match(/^(.+)_(\d+)$/);
                    id_template = match[1];
                    id = parseInt(match[2]);
                    if (id > maxid) maxid = id;
                });

                var id = id_template + '_' + (maxid + 1);
                var new_li = $('<li/>').append(
                    $('<img/>').attr('src', newRepr['thumbnail']).attr('width', '50').attr('height', '50').add(
                        $('<label/>').attr('for', id).append(
                            $('<input class="mediasortedm2m" type="checkbox" checked="checked" />').attr('id', id).val(newId)
                        ).append($('<span/>').text(' ' + html_unescape(newRepr['label'])))
                    )
                );
                mediasortedm2m.append(new_li);

                win.close();
            };
        }
    });
})(jQuery);
