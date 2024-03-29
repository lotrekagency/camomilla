# CHANGELOG



## v5.8.6 (2023-09-25)

### Chore

* chore: always try to upload pypi ([`f92880c`](https://github.com/lotrekagency/camomilla/commit/f92880c17c936af0793956b704f1511a37d66d30))

* chore: update testing workflow ([`0b9e073`](https://github.com/lotrekagency/camomilla/commit/0b9e073559fada746647ed089248ff43d4e0d567))

* chore: better job step splitting ([`9d158d5`](https://github.com/lotrekagency/camomilla/commit/9d158d5836431171fb1a6fd11f4f7dc90b22b10f))

* chore: fix run build in cd.yml ([`2cf8a30`](https://github.com/lotrekagency/camomilla/commit/2cf8a3086cd28c0b57679692645e45a3f6be025d))

* chore: fix build run statement ([`d9d5f14`](https://github.com/lotrekagency/camomilla/commit/d9d5f14567c24f4713b223a896ff6d11c26b5147))

* chore: decouple package build from version tagging in cd.yml ([`4c96a8e`](https://github.com/lotrekagency/camomilla/commit/4c96a8e4df9b9795ec06aff479f24f05ebeb599b))

* chore: set force release options to release workflow ([`852f37f`](https://github.com/lotrekagency/camomilla/commit/852f37f53c3e3e3eef2e80b1fe1cae07ed8f7a08))

* chore: update permissions on release githubworkflow ([`e857992`](https://github.com/lotrekagency/camomilla/commit/e85799203e6a13182b61b0457ee1a48e973e76ff))

* chore: update permissions on release githubworkflow ([`dd9bf9d`](https://github.com/lotrekagency/camomilla/commit/dd9bf9d0ccbb2759d0f214c179d61dc997a78f9b))

* chore: update cd ([`c936605`](https://github.com/lotrekagency/camomilla/commit/c9366057684d928bd8b334affaa0264637ccd4e4))

* chore: update cd ([`1640461`](https://github.com/lotrekagency/camomilla/commit/1640461b7bacc9851a2c8860b2cdb80e32744500))

* chore: cd remove bad config ([`e2e2d45`](https://github.com/lotrekagency/camomilla/commit/e2e2d45420ffd13c95e697e397c6100fa272e410))

* chore: fix versioning ([`54f3868`](https://github.com/lotrekagency/camomilla/commit/54f38685cc0d69bc33304138c3e92998269d134f))

* chore: make cd and ci triggerable ([`8cf368b`](https://github.com/lotrekagency/camomilla/commit/8cf368bf39d3159454eb4b5b1bfecd50cf06a8f9))

* chore: move to pyproject.toml ([`fab43fd`](https://github.com/lotrekagency/camomilla/commit/fab43fd5bbf2a70b9d80fe20fa083a7e00bee663))

* chore: fic CD pipeline not getting config file for semantic release ([`e851c7e`](https://github.com/lotrekagency/camomilla/commit/e851c7ead9ce643f77c368eebfabb0eb5ec979a0))

* chore: update semantic-release and CD pipe ([`6479126`](https://github.com/lotrekagency/camomilla/commit/6479126b6da3db96a011f708dbbb85d138c26bfb))

### Fix

* fix: fix setup.cfg ([`621db85`](https://github.com/lotrekagency/camomilla/commit/621db857f20657b2b9a030283aa323b02280d48a))


## v5.8.5 (2023-03-07)

### Fix

* fix(related): nest mixing now is taking depth directly from constructor ([`63c5ae5`](https://github.com/lotrekagency/camomilla/commit/63c5ae5d1c8444bec8b68afac20e2e57fb3b944e))

* fix(related): fix related serializer trying to set queryset on readonly models ([`bd2eb4f`](https://github.com/lotrekagency/camomilla/commit/bd2eb4f9ce2eee5d9807ff656acee6e2c1584170))


## v5.8.4 (2022-12-21)

### Fix

* fix: fix jsonPatch mixin for trans jsons ([`e0c9236`](https://github.com/lotrekagency/camomilla/commit/e0c9236994fa2a776702c83f14db7496fdcc6450))


## v5.8.3 (2022-12-21)

### Fix

* fix: fix potential recursion error in NestMixin and take nesting depth from settings ([`647114c`](https://github.com/lotrekagency/camomilla/commit/647114c0b32a556773fe657929a9e3d86254b295))

* fix: fix recursive nestmixin functions ([`e83586e`](https://github.com/lotrekagency/camomilla/commit/e83586eba127e970b714d78b2cb0ff353731d6fc))

### Unknown

* Merge branch &#39;master&#39; of github.com:lotrekagency/camomilla ([`91fe6c1`](https://github.com/lotrekagency/camomilla/commit/91fe6c1d9c2c8994964a44a173e86677e0d6910c))


## v5.8.2 (2022-12-21)

### Fix

* fix: fix nested translations mixins ([`2c17ed8`](https://github.com/lotrekagency/camomilla/commit/2c17ed86d2169df67f2e14b37518e8dc16b6a121))


## v5.8.1 (2022-12-20)

### Fix

* fix: fix potential recursion error in NestMixin ([`f337155`](https://github.com/lotrekagency/camomilla/commit/f33715549ecb2555eba07ddc2a676e314e48c235))

* fix(media): allow json parser in media for patch requests without files ([`b117229`](https://github.com/lotrekagency/camomilla/commit/b1172297f22cf032c41efefe6a58b206c34d5e2b))

* fix: show all permissions on profile serializer ([`fb1dc5e`](https://github.com/lotrekagency/camomilla/commit/fb1dc5ee3e27dec4d382e6a06a60599ab82cff1e))

* fix(media): allow json parser in media for patch requests without files ([`00b1d24`](https://github.com/lotrekagency/camomilla/commit/00b1d24a0de19c3a4cfb0bbeafba9e48e06c46ce))

### Unknown

* Merge pull request #15 from lotrekagency/hotfix/userpermissions

Added all permissions array to user profile ([`15891b1`](https://github.com/lotrekagency/camomilla/commit/15891b1d52d8d1b493822d902fc0bdffbc921770))

* Merge branch &#39;hotfix/userpermissions&#39; of github.com:lotrekagency/camomilla into hotfix/userpermissions ([`aba3d89`](https://github.com/lotrekagency/camomilla/commit/aba3d89b0894da44acf5b6f2bb6cd8de1487fb04))


## v5.8.0 (2022-12-20)

### Chore

* chore: fix black ([`c092aab`](https://github.com/lotrekagency/camomilla/commit/c092aabed9ca3042f092c4b11d97951bfb6d9afe))

### Feature

* feat(rest_framework): go down in nested relation with updatable serializers, DEFAULT_NEST_DEPTH = 10 ([`d22ea66`](https://github.com/lotrekagency/camomilla/commit/d22ea664820e8b5843435aaa7c279502888992f0))

* feat: optimize many related field to fetch all existing objects ([`8ba3982`](https://github.com/lotrekagency/camomilla/commit/8ba39828c3dbf3c16c5cc89c38e69fb939c8a062))

### Fix

* fix: fallback media api translations ([`e279f7a`](https://github.com/lotrekagency/camomilla/commit/e279f7ad4eec933ddb4f43b85f0498d1fbf3d17b))

* fix: fix patch method overriding json field ([`faf7e4b`](https://github.com/lotrekagency/camomilla/commit/faf7e4b5586801639d3633e6db37c0d1e95d9d15))

* fix: show all permissions on profile serializer ([`e2a0116`](https://github.com/lotrekagency/camomilla/commit/e2a011602520945c9835091797d3d7ca508f0f52))

* fix: handle ints in many related fields ([`eb7140a`](https://github.com/lotrekagency/camomilla/commit/eb7140a03d0b933939fd6b163744420bc8f9cf59))

* fix(serializers): added BaseModelSerializer to default serializers of RelatedFields ([`e9a37b5`](https://github.com/lotrekagency/camomilla/commit/e9a37b54c0e15acdd7c95ed008b6b5b9722d13c5))

* fix(page): added safe page translation getter in get_page ([`bea64d7`](https://github.com/lotrekagency/camomilla/commit/bea64d7890d9713f1d9043902b9dd9cfe30f7ce9))

* fix(db): added trigram extension in migrations ([`bdadea1`](https://github.com/lotrekagency/camomilla/commit/bdadea19f56bfe1a518f020ec18615e448a3df2d))

### Unknown

* deps: update django hvad dep ([`705f057`](https://github.com/lotrekagency/camomilla/commit/705f05723b0a61b426c3cda011f7be4a5d028916))

* Merge branch &#39;hotfix/trigram&#39; ([`cfea914`](https://github.com/lotrekagency/camomilla/commit/cfea914e9fd44ea0486640db9bcc48594498f50e))

* Merge branch &#39;master&#39; into hotfix/trigram ([`c899467`](https://github.com/lotrekagency/camomilla/commit/c89946764ab9439fabcb4bc03d509ab20d57ff93))


## v5.7.7 (2022-08-12)

### Fix

* fix: fix bad typechecking in BaseModelSerializer ([`5063abf`](https://github.com/lotrekagency/camomilla/commit/5063abfddb47e79cd7ec7b16ce43536021138f55))


## v5.7.6 (2022-08-12)

### Fix

* fix: fix BaseModelSerializer related field injectig serializer kwargs in wrong class ([`a212c2f`](https://github.com/lotrekagency/camomilla/commit/a212c2fa5fd611fb63899a05026a78ff5f3d4d02))


## v5.7.5 (2022-08-11)

### Fix

* fix: explicit default_auto_field in app config to prevent unwanted migrations ([`ec33de8`](https://github.com/lotrekagency/camomilla/commit/ec33de87be8f7fc7fc466070e8fe20b7e75ef438))


## v5.7.4 (2022-08-02)

### Chore

* chore: update requirements ([`b1cfeeb`](https://github.com/lotrekagency/camomilla/commit/b1cfeeb8fe284d04be5dd60c404089c17ffd3f28))

### Fix

* fix: added missing migrations ([`e57989e`](https://github.com/lotrekagency/camomilla/commit/e57989e7174374bdcff19d042956327e12b65fe4))

* fix: fix media migration to be compliant with hvad ([`dc5e83a`](https://github.com/lotrekagency/camomilla/commit/dc5e83ad0d639024319a49ac00b01f8845fbe9f1))

* fix: fix makefile ([`925a270`](https://github.com/lotrekagency/camomilla/commit/925a2706f00c2b6ab5cc9055a557192a4bbd8d4a))

* fix: added missing migrations for django 4 ([`8a79998`](https://github.com/lotrekagency/camomilla/commit/8a79998e39c9555385ab0d9e87f299b0ede2883d))

### Test

* test: fix tests ([`79440a2`](https://github.com/lotrekagency/camomilla/commit/79440a2352f5fa34c072245049d7ede4d12166e3))


## v5.7.3 (2022-05-16)

### Chore

* chore: flake8 fix ([`f83b38a`](https://github.com/lotrekagency/camomilla/commit/f83b38a85c36a05f705a80530751b0d4a31ad26b))

* chore: update ci test matrix to test camomilla also on django 3 and 4 ([`226ed58`](https://github.com/lotrekagency/camomilla/commit/226ed58a3734c918b7aaf3b48a9fed5489cddc0c))

### Fix

* fix: fix Arrayfield import ([`2cfdaca`](https://github.com/lotrekagency/camomilla/commit/2cfdacacb63d59cea79ae59f0c3d9839efe56088))

* fix: fix jsonfield imports ([`be4b566`](https://github.com/lotrekagency/camomilla/commit/be4b56622df269ee5d200dc5666536b39e7fe0cc))


## v5.7.2 (2022-05-13)

### Fix

* fix: fix get page to work with new hvad ([`2cd8b89`](https://github.com/lotrekagency/camomilla/commit/2cd8b8948df44fd82c214835770e92b10a3f5512))

* fix: fix camomilla filter content to work with new hvad ([`0193509`](https://github.com/lotrekagency/camomilla/commit/019350929c19cccdfedbdfc2b493039484a08400))

* fix: update camomilla template to support new django admin static ([`92afbc0`](https://github.com/lotrekagency/camomilla/commit/92afbc07a1345cf19ed4a5a83317f7658b008804))

* fix: fix gettext_lazy import deprecated in django4 ([`626dfe1`](https://github.com/lotrekagency/camomilla/commit/626dfe16a9fb6457e463ac995eb9d4d809c51e22))

### Unknown

* deps: update djsuperadin dependency ([`8089b1e`](https://github.com/lotrekagency/camomilla/commit/8089b1e5fa6b90e4712559a9635027d6a908c3c9))

* deps: update lotrek-django-hvad deps and sintax ([`996f6bf`](https://github.com/lotrekagency/camomilla/commit/996f6bfdd73c4b6ea8ece811a4138ba9cc7f8a00))

* deps: update deps to bring compatibility with django 4 ([`fc7dade`](https://github.com/lotrekagency/camomilla/commit/fc7dade2f949c363ec8101b4ea484e791f27d52b))


## v5.7.1 (2022-03-30)

### Chore

* chore: black . ([`5539ed2`](https://github.com/lotrekagency/camomilla/commit/5539ed25d598ed766587e787ff906c9afae93de7))

### Fix

* fix: fix circular import error ([`8b3f6ff`](https://github.com/lotrekagency/camomilla/commit/8b3f6ff2d7a01a2f138506ef4ad94fe78b691521))

* fix: fix session login urls ([`2688c1a`](https://github.com/lotrekagency/camomilla/commit/2688c1aae082654bebd84f3bfd8f2b74104fa930))

* fix: fix drf session authentication ([`538e709`](https://github.com/lotrekagency/camomilla/commit/538e709dcc8fd2799b4063c265687b2e0315c076))

### Test

* test: fix test ([`5f0bee8`](https://github.com/lotrekagency/camomilla/commit/5f0bee833da4a50d6b35bf279c931dfe47a43411))


## v5.7.0 (2022-03-14)

### Chore

* chore: black . ([`dba13f4`](https://github.com/lotrekagency/camomilla/commit/dba13f4b89c5c219c6c765e79066c2b210a89cd3))

* chore: black . ([`32789cd`](https://github.com/lotrekagency/camomilla/commit/32789cd38287ea14df6e6960086439b3037ccb04))

* chore: migrate db with ordering and meta ([`560be53`](https://github.com/lotrekagency/camomilla/commit/560be537c29c34ddf3a97e7aec4ca4e8f077797c))

### Feature

* feat: added ordering to Articles Categories and Pages ([`8cb6d75`](https://github.com/lotrekagency/camomilla/commit/8cb6d752e462462c37add877c056827fddb491cc))

* feat: added meta to Articles Categories and Pages ([`f859c37`](https://github.com/lotrekagency/camomilla/commit/f859c370add3b34c081edccc4925c0cd99064d42))

* feat: meta mixin for models 🦹 ([`88c4b4a`](https://github.com/lotrekagency/camomilla/commit/88c4b4afbfc042ea024c9f4ab6090ccb5b73b272))

* feat: added ordering mixin for rest framework inspired by django adminsortable2 ([`cb619bc`](https://github.com/lotrekagency/camomilla/commit/cb619bcb10650174d8e01835fdb9ecf44ece81a7))

### Fix

* fix: fix meta mixin methods ([`7d7e3a8`](https://github.com/lotrekagency/camomilla/commit/7d7e3a80bda93a5faec92ebe52ed7be28635790d))

* fix: fixed reverse ordering in update_order endpoint ([`b8ae096`](https://github.com/lotrekagency/camomilla/commit/b8ae0962bdb75895945b0cc696fb64647e079b31))

* fix: fix pagination ordering without default order field ([`ca07303`](https://github.com/lotrekagency/camomilla/commit/ca07303c951fe4e6142a8af74ff282d0f90c67c2))


## v5.6.1 (2022-03-01)

### Fix

* fix: fix pagination mixin to provide order filter and search also for unpaginated queries ([`62e8b01`](https://github.com/lotrekagency/camomilla/commit/62e8b01433aac97a5b70de6197f7bb957e5abf46))

### Test

* test: fix api test after ordering ([`9602ce1`](https://github.com/lotrekagency/camomilla/commit/9602ce123665b489b3c79f228c30435f71ad01e6))


## v5.6.0 (2022-02-26)

### Feature

* feat: added permission classes to media api ([`558cac2`](https://github.com/lotrekagency/camomilla/commit/558cac2a2b852dcd76d2ad20ce1ab14b4ccb01b0))

* feat: auto-order pagination mixins ([`125dd71`](https://github.com/lotrekagency/camomilla/commit/125dd71b05faa6554a9def76bd664b837ca8d8fe))

* feat(serializers): automagically 🧙 create nested serializers at runtime avoiding the need of declaring RelatedField classes ([`4748786`](https://github.com/lotrekagency/camomilla/commit/47487860494b56f5fdbff11b4bcc1790e2f9581a))

### Fix

* fix: fix paginate stack oredering ([`685cf8d`](https://github.com/lotrekagency/camomilla/commit/685cf8dbca2aae00fd2536ed1e1dca6696e88734))


## v5.5.2 (2022-02-14)

### Fix

* fix: fix djsuperadmin reverse url ([`035d377`](https://github.com/lotrekagency/camomilla/commit/035d377ef9c4dfc25516103542c0aea28a0445a6))

### Unknown

* Merge branch &#39;master&#39; of github.com:lotrekagency/camomilla ([`7dfbe03`](https://github.com/lotrekagency/camomilla/commit/7dfbe03c27ae5f53b4d7c7b6e880bc9899ba66ea))


## v5.5.1 (2022-02-14)

### Chore

* chore: black . ([`a811c72`](https://github.com/lotrekagency/camomilla/commit/a811c72de2fa37c296215f41dec755405edbf28f))

### Fix

* fix: fix RelatedField allow_insert condition ([`90ba04f`](https://github.com/lotrekagency/camomilla/commit/90ba04f2520bf131c95145121362984535f367e2))

* fix: fix serarchfield for article viewset ([`2c9cda4`](https://github.com/lotrekagency/camomilla/commit/2c9cda4f387bc4bbc5909f7f40ebd484591cb402))

* fix: added missing migration ([`a018f0f`](https://github.com/lotrekagency/camomilla/commit/a018f0f125e68548492d3fd74a5cd8bddda61293))

* fix: Refactor filefield and fix bad return value ([`1f1a36a`](https://github.com/lotrekagency/camomilla/commit/1f1a36aaa2fad7e43a348ef2513e1aaabdddaae3))

* fix: fix related field trying to insert new values all the time ([`2465598`](https://github.com/lotrekagency/camomilla/commit/246559814ef351d2cd010fd6f7385777dd075cf2))

### Unknown

* Merge branch &#39;master&#39; of github.com:lotrekagency/camomilla ([`0dc22e3`](https://github.com/lotrekagency/camomilla/commit/0dc22e3b479f8c5b070407c1974dd752ba03d49f))


## v5.5.0 (2022-02-12)

### Chore

* chore: black . ([`920791d`](https://github.com/lotrekagency/camomilla/commit/920791d79b31a9b603c07c86c6bf1bf450629379))

* chore: black . ([`df1a32a`](https://github.com/lotrekagency/camomilla/commit/df1a32ab1d7bd9b3441e17d1aa96ac3b82519c01))

### Feature

* feat(api): brand new serializators views and permissions for users endpoint ([`0f5b824`](https://github.com/lotrekagency/camomilla/commit/0f5b824c0c614d9ec8fbb1ffd04644e3d30e774c))

* feat(api): added trigram search mixin to medias ([`0002c8b`](https://github.com/lotrekagency/camomilla/commit/0002c8b40a317b3d6bae64c1c12764e31e59cb6c))

### Fix

* fix: fix File fields imports ([`3a0af76`](https://github.com/lotrekagency/camomilla/commit/3a0af764afefc88336bcb0646e13dc3c9deee609))

* fix: added creation logics for Related fields ([`56f20a5`](https://github.com/lotrekagency/camomilla/commit/56f20a5df522035ef5bbdca6e8c67bfa40daf274))

* fix: integrate Camomilla fields in Base model serializers ([`3556d33`](https://github.com/lotrekagency/camomilla/commit/3556d33c7343208b9f7b0e380bb1614c24298169))

* fix: added FileField and ImageField to fix drf Fields ([`7fc3160`](https://github.com/lotrekagency/camomilla/commit/7fc3160b493cc102ffa1be029e651bc3196266cc))

* fix: article permalink is now slugfield to prevent bad inputs ([`aafd92c`](https://github.com/lotrekagency/camomilla/commit/aafd92cb518fe5e768ad3fd6f515af0c8599747a))

* fix: fix article serializer missing categories ([`93b4284`](https://github.com/lotrekagency/camomilla/commit/93b42840980da194dd6b40646d7d5685c7da930a))

### Unknown

* Merge pull request #9 from lotrekagency/hotfix/searchconf

Added Trigram search mixin ([`3ff1bd2`](https://github.com/lotrekagency/camomilla/commit/3ff1bd2f9a6b21733b27ae437a897e0458a6e129))


## v5.4.2 (2022-01-18)

### Chore

* chore: change semantic release conf ([`944d36f`](https://github.com/lotrekagency/camomilla/commit/944d36f90038f0533bcf08908dddc9baef3e56b8))

### Fix

* fix: fix versioning ([`39b5226`](https://github.com/lotrekagency/camomilla/commit/39b522637ff79c7ff05237d1ad85e1cae26d2a94))

* fix: added min max range to requirements ([`6841054`](https://github.com/lotrekagency/camomilla/commit/6841054d71c0704919b446eb8ed542d3fb08a873))

### Unknown

* Merge branch &#39;master&#39; of github.com:lotrekagency/camomilla ([`f713e25`](https://github.com/lotrekagency/camomilla/commit/f713e252b5ca129fbce2c14841af026ebdf0f4a1))


## v5.4.1 (2022-01-17)

### Fix

* fix: loosen the range of requirements package versions ([`96d491b`](https://github.com/lotrekagency/camomilla/commit/96d491b4ff0aba269624eb7a27b1f3cd55946721))


## v5.4.0 (2022-01-13)

### Chore

* chore: black + remove unused imports ([`f6884cc`](https://github.com/lotrekagency/camomilla/commit/f6884cce0836d5dcf74d204e5523785ddc435a50))

* chore: fix coverage report ([`c009cae`](https://github.com/lotrekagency/camomilla/commit/c009caed0aef9cc70a10b864238def471eef16be))

### Feature

* feat(media): added mime_type column to media model ([`4771068`](https://github.com/lotrekagency/camomilla/commit/4771068d2e54779a3d6e38ee9b447fb04c73539c))

* feat(api): added search to medias ([`905661d`](https://github.com/lotrekagency/camomilla/commit/905661d874b5ff2e22ea8b508c46d1ccfc70c0e7))

* feat(media): added option to override Media file on update from api to maintain same url ([`8d6371f`](https://github.com/lotrekagency/camomilla/commit/8d6371ff94e460f2e84efde45882d7d192b7cce6))

### Fix

* fix(media): added opetation to db  migration to recalc old media with the new mime_type feature ([`a7afd2d`](https://github.com/lotrekagency/camomilla/commit/a7afd2d53ba2b2f27d0d06fb6dba131368fdcc6e))

* fix(media): mime filter parsing works also in folder viewset ([`4149e92`](https://github.com/lotrekagency/camomilla/commit/4149e92e6c67e5f96219f02859a3aaa3f748553d))

### Unknown

* Merge pull request #6 from lotrekagency/feature/media

Added mime type and search to Medias ([`39767ec`](https://github.com/lotrekagency/camomilla/commit/39767ec9057ecd549ea8936738f2749d8beb7389))


## v5.3.0 (2021-12-17)

### Chore

* chore: fix ci/cd ([`682f200`](https://github.com/lotrekagency/camomilla/commit/682f20025f2053dd644a0a3b83ee91c6f6d0116a))

* chore: fix ci/cd ([`0a6daf4`](https://github.com/lotrekagency/camomilla/commit/0a6daf455a55372ea93e3bf728213d3843a8cd25))

* chore: update readme ([`a75daee`](https://github.com/lotrekagency/camomilla/commit/a75daeef290337f423a4fc27b0efd942aca8bde6))

* chore: update readme ([`6bde3c8`](https://github.com/lotrekagency/camomilla/commit/6bde3c85a2678e88176a60ff7182e7210a42d29c))

* chore: update ci job names ([`991280c`](https://github.com/lotrekagency/camomilla/commit/991280cdff420462f65267c28003e55314fae728))

### Feature

* feat(api): handle multisort on PaginateStackMixin ([`40080f4`](https://github.com/lotrekagency/camomilla/commit/40080f4542c8e0dd4c8b36bb5cf5de6e078c3314))

### Unknown

* Merge pull request #5 from lotrekagency/feature/multiplesort

Handle multisort on PaginateStackMixin ([`33616c7`](https://github.com/lotrekagency/camomilla/commit/33616c74ebc908d2f0ef7bc2fd98e2d3a3da5cfc))


## v5.1.0 (2021-12-17)

### Chore

* chore: added release to ci ([`bb99d98`](https://github.com/lotrekagency/camomilla/commit/bb99d984b22128e78597c481128719ab36567faf))

* chore: removed django 3 compatibility ([`f9420c5`](https://github.com/lotrekagency/camomilla/commit/f9420c50aa3e3b8a6f6339ae61de343d7fae4ef9))

* chore: update ci ([`08dadb3`](https://github.com/lotrekagency/camomilla/commit/08dadb3f78ff27aecef4215ed085d54a8dc85155))

* chore: update ci ([`765e5b5`](https://github.com/lotrekagency/camomilla/commit/765e5b527d0e4733626b2038a2fa08c26b54fc8f))

* chore: update ci ([`9536ded`](https://github.com/lotrekagency/camomilla/commit/9536ded0819cb3c364e915efe0189ed1cf49c2f2))

* chore: update ci ([`c38c634`](https://github.com/lotrekagency/camomilla/commit/c38c6347725f887efcb634320d9026bc9d934f85))

* chore: fix ci ([`9701dc1`](https://github.com/lotrekagency/camomilla/commit/9701dc1b4d4794bc512429a9c56307ee3473a3ed))

* chore: update ci ([`723f8f3`](https://github.com/lotrekagency/camomilla/commit/723f8f3d296784c5ab85c596abbbe007731fd060))

* chore: update ci ([`b08a52a`](https://github.com/lotrekagency/camomilla/commit/b08a52a983ac011f94f40d50d22a91616743bbd5))

* chore: add flake8 settings ([`381b560`](https://github.com/lotrekagency/camomilla/commit/381b5608b91fb17df4386722c1d1375f9ba7f04b))

* chore: fix flake8 errors ([`440d214`](https://github.com/lotrekagency/camomilla/commit/440d21463ff7e70617e538d5c3fbc2814798c5dd))

* chore: update ci.yml ([`3a21126`](https://github.com/lotrekagency/camomilla/commit/3a21126c60cea44e41fc1ce5ceb1ceeaf763e083))

* chore: add ci tests ([`1924786`](https://github.com/lotrekagency/camomilla/commit/1924786413180679f9c59c2d53798b5c0258976d))

### Feature

* feat: added image properties into media model ([`09cb481`](https://github.com/lotrekagency/camomilla/commit/09cb4818b2e3207eab7a12361f5e273b17edd1d0))

* feat: option to remove pagination on views ([`3e6fc48`](https://github.com/lotrekagency/camomilla/commit/3e6fc489db8b01f488ffebedd93f614c01d9e8d3))

### Fix

* fix: fix sqlite compatibility problems ([`4cde4fc`](https://github.com/lotrekagency/camomilla/commit/4cde4fc6c5f0e0b0d76e2020943de6d0bc973a49))

* fix: fix app name ([`13bb12d`](https://github.com/lotrekagency/camomilla/commit/13bb12d75bc9072a9ff150a7b408157f022c9299))

* fix: added search field to article viewset ([`1bd4b5f`](https://github.com/lotrekagency/camomilla/commit/1bd4b5f0681885b19bb2043d7622c8b3e77b9689))

* fix: fix articles and pages serializers requiring RelatedField fields. ([`c4fd330`](https://github.com/lotrekagency/camomilla/commit/c4fd330fb06dc3d49de4100865376a9eedb3f6f6))

### Test

* test: fix test conf ([`140b658`](https://github.com/lotrekagency/camomilla/commit/140b658dcd829c65ae126eb4c8ce886f3d098543))

* test: add psycopg2 to dev-requirements ([`2d9004a`](https://github.com/lotrekagency/camomilla/commit/2d9004af770dec2db15f48e9dee7ea203309e84e))

* test: update flake8 ([`0f9ed23`](https://github.com/lotrekagency/camomilla/commit/0f9ed23297cdb812e43c99b023b7a7810ab7e3ec))

* test: fix testing ([`31e2077`](https://github.com/lotrekagency/camomilla/commit/31e2077c024056158a06454c53a9035e9db437a2))

### Unknown

* Merge branch &#39;master&#39; of github.com:lotrekagency/camomilla ([`296623a`](https://github.com/lotrekagency/camomilla/commit/296623a161d056b7539de08d2a2f06d8cebddd57))

* Merge pull request #3 from lotrekagency/hotfix/search_field

Add search field to article viewset ([`b8a9888`](https://github.com/lotrekagency/camomilla/commit/b8a988865cb048917eadb68ba8a843cb058264bc))

* Merge pull request #4 from lotrekagency/feature/image_properties

Add image properties to Media model ([`b4677c5`](https://github.com/lotrekagency/camomilla/commit/b4677c52dbcd0d1b32072cdaafe57cf3f0aa50a0))

* Merge pull request #2 from lotrekagency/hotfix/no_pages

Added option to disable pagination on views ([`2e32c18`](https://github.com/lotrekagency/camomilla/commit/2e32c1899d86278d8c3531ab156ca1dee3549fd4))


## v5.0.3 (2021-10-26)

### Chore

* chore: Move package version to __init__.py ([`e17c97a`](https://github.com/lotrekagency/camomilla/commit/e17c97af18d0453da4fd959d69ab5d3d567a26a4))

* chore: Replace git packages dependencies with pypi packages ([`1b0672e`](https://github.com/lotrekagency/camomilla/commit/1b0672ec66b1624fd7923a8f25710b1e81835c10))

* chore: Use semantic versioning for package publishing pipe ([`35b9933`](https://github.com/lotrekagency/camomilla/commit/35b9933f8b027dee42e1089e6d5bdc5f80fc6721))

### Unknown

* Merge branch &#39;master&#39; of github.com:lotrekagency/camomilla ([`3b40fd5`](https://github.com/lotrekagency/camomilla/commit/3b40fd5a4a649ed33163950ebab225bd20529d45))

* added MIT license ([`2c517c5`](https://github.com/lotrekagency/camomilla/commit/2c517c57d60f7de8cf53aee16c5ad98ceb17b888))

* Merge pull request #1 from lotrekagency/hotfix/pagination

Fix some pagination issues ([`e892d08`](https://github.com/lotrekagency/camomilla/commit/e892d08fb22faa43f37da45a7f28e3b06942943c))

* change pages range to pages count ([`a1185dc`](https://github.com/lotrekagency/camomilla/commit/a1185dc2ab242ab370bf7738b94728fe92f9eed3))

* fix searchvector arguments ([`ddc7353`](https://github.com/lotrekagency/camomilla/commit/ddc7353abbca5a8a60342c35b219b23f1a2106e8))

* added mediaListSerializer to decrease db stress on list call ([`1ee30d6`](https://github.com/lotrekagency/camomilla/commit/1ee30d62f3216a071d7509e6760dc05851a0ecb6))

* little refactor of serializers and views to centralize controls of mixins ([`fdfea21`](https://github.com/lotrekagency/camomilla/commit/fdfea21ebd26e19840f736d57fb5a862373cc7db))

* fix multipart parser ([`76e7549`](https://github.com/lotrekagency/camomilla/commit/76e754917b05742f4255a01f4f04b853cd1e86d6))

* new logic for multipart parser, added array path indexing ([`fbf88b2`](https://github.com/lotrekagency/camomilla/commit/fbf88b2b186fc6f0b1f1eba6ccd663bb106a791e))

* Merge branch &#39;feature/camomillareloaded&#39; ([`ec89be9`](https://github.com/lotrekagency/camomilla/commit/ec89be96c865bfa7dad98558a9d49324ab0dcf2a))

*  add migration ([`65db750`](https://github.com/lotrekagency/camomilla/commit/65db750590f85f6aec399df1757821b026dd8b38))

* removed some default confs ([`5d52e4e`](https://github.com/lotrekagency/camomilla/commit/5d52e4eb3d050bd16dfb5c5494a0552ee41841a9))

* removed jwt&#39; ([`d0f2d47`](https://github.com/lotrekagency/camomilla/commit/d0f2d476772b6f56c48e758e28fc6a401511f828))

* wip on serializers and views ([`5e982a4`](https://github.com/lotrekagency/camomilla/commit/5e982a4adc6229c51fdb9ef691ea6e8ca4269e66))

* wip on trans helpers ([`3dda877`](https://github.com/lotrekagency/camomilla/commit/3dda877f839d9e7d50310082600892f95e2b2f01))

* removed ExpandedArticleSerializer ([`c433647`](https://github.com/lotrekagency/camomilla/commit/c43364761b5ff4cdbeac910e1dde50310c55682a))

* remove trash mixins ([`cc0c4f2`](https://github.com/lotrekagency/camomilla/commit/cc0c4f27a12a3e4f5ee609d37f6f0beb824073cb))

* better translation initializaion ([`36c2e80`](https://github.com/lotrekagency/camomilla/commit/36c2e8036bdc7e6ec27b726799332470897661c2))

* fix related field choices visualizations drf ([`88669db`](https://github.com/lotrekagency/camomilla/commit/88669db06beb6a013360a04bc0e914e45a9c2923))

* refactorized serializers ([`f0105a3`](https://github.com/lotrekagency/camomilla/commit/f0105a38ee7f5d1c49f68c657f08bdab26ab5d04))

* ArticleView rewrite ([`f83f07f`](https://github.com/lotrekagency/camomilla/commit/f83f07f89cf5ff43c5c6e61f2833e2e968f6fe86))

* added RelatedField serializer ([`6acead6`](https://github.com/lotrekagency/camomilla/commit/6acead6019ee6941c15fbc37e6338c029071322a))

* conditional pagination ([`c44ba0c`](https://github.com/lotrekagency/camomilla/commit/c44ba0cf991d3e40400ed91c549c77b1e1cfc20b))

* Fixed parser for media update ([`1941029`](https://github.com/lotrekagency/camomilla/commit/19410296b6417d29115eae160a7134df2d0c08b7))

* remove pagination from folders ([`6aea267`](https://github.com/lotrekagency/camomilla/commit/6aea26747f3dfc654ee73dbf9c3ab0d1d2f80fc3))

* added pagination and some upgrade to media models ([`2896e4b`](https://github.com/lotrekagency/camomilla/commit/2896e4b3c8ba76e2c18a26672eacafa98b4774dd))

* big refactor code structure ([`9cd06c5`](https://github.com/lotrekagency/camomilla/commit/9cd06c5043e3179d5f73e7b416a4a86450b3ab2e))

* added token api endpoint and permissions to user serializer ([`a798c6a`](https://github.com/lotrekagency/camomilla/commit/a798c6a4fb85b398182f0f8e60ee1ad56eb84023))

* Added context in MediaFolderViewset for MediaSerializer ([`aaf8b86`](https://github.com/lotrekagency/camomilla/commit/aaf8b861289b548c96da013569f94ea95bd1c363))

* Added context to MediaDetailSerializer ([`52b815a`](https://github.com/lotrekagency/camomilla/commit/52b815abf7e3ba767692b14e1be8b22193190c1e))

* addded try block to make_thumbnails Media ([`e7e44db`](https://github.com/lotrekagency/camomilla/commit/e7e44db57d1cdf4da931f1b671aa62794a400ece))

* wix wrong slugify import ([`d031ab4`](https://github.com/lotrekagency/camomilla/commit/d031ab489ba99d565e6a3eaf4c1e816fa9c94f18))

* fix slugmixin missing slugify dependency ([`124e054`](https://github.com/lotrekagency/camomilla/commit/124e05452fc7e477a52819d370f065b3a791dd5b))

* Fix models ([`7e9ce16`](https://github.com/lotrekagency/camomilla/commit/7e9ce16bbbc8ace126a32682123dcd5aa87c9c26))

* Remove useless print ([`37e2432`](https://github.com/lotrekagency/camomilla/commit/37e24327cd53c34c2a32f9c226b4e69004924298))

* Autogenerate identifier for articles ([`0124b1b`](https://github.com/lotrekagency/camomilla/commit/0124b1b9a1fcc14df72bf0433e6aeecc3feec899))

* More tests ([`4be200b`](https://github.com/lotrekagency/camomilla/commit/4be200b3d7096bfecf8011dcac2ae3b4892f2bdb))

* Update requirements.txt with Pillow 6.2.0 ([`211a4c4`](https://github.com/lotrekagency/camomilla/commit/211a4c42fe9f2b3984f6e0a403e4fc3bd3e5dbd0))

* Update Pillow ([`dac2fc7`](https://github.com/lotrekagency/camomilla/commit/dac2fc70aefb4b7d0380147a1e9b3edce123eda3))

* Fix filters ([`88a1bb6`](https://github.com/lotrekagency/camomilla/commit/88a1bb6c90ec20e2cb5d2359f23b588ce0a9afba))

* Update dependencies ([`a9c7264`](https://github.com/lotrekagency/camomilla/commit/a9c72647ddc14bdf0190804ec8169639d5cc885c))

* Remove some useless code and add api tests ([`f26ae1a`](https://github.com/lotrekagency/camomilla/commit/f26ae1a192c76629c4d941c58298175f1807e363))

* Move tests outside lib folder ([`075292c`](https://github.com/lotrekagency/camomilla/commit/075292cac5cba987aa0b92cd8d578012a388548c))

* Restore with new django-hvad ([`b6b6dae`](https://github.com/lotrekagency/camomilla/commit/b6b6dae5666f5f5431581fe3b3a9b939bc3c2d56))

* First part of tests ([`553be4b`](https://github.com/lotrekagency/camomilla/commit/553be4b444b5c6599510c1b0a56185eebfa1c198))

* Make JWT token valid for 300 days ([`aca3494`](https://github.com/lotrekagency/camomilla/commit/aca34943c564c8632edb1453b61401088ff81b07))

* Add djsuperadmin ([`499286b`](https://github.com/lotrekagency/camomilla/commit/499286b849d237ca248fb25bb567d5cf04006a70))

* Switch to djangohvad 2 ([`0cd9ed3`](https://github.com/lotrekagency/camomilla/commit/0cd9ed370e90bf438df2098b24d9422dda8c2538))

* Road to 5 ([`c833790`](https://github.com/lotrekagency/camomilla/commit/c833790fe85d3581505afacfe6ed150b25843280))

* Fix DEFAULTS ([`a04f8a1`](https://github.com/lotrekagency/camomilla/commit/a04f8a1bc60a08dfe8772c90cfa8f62864ba51a7))

* Move middlewares to DjLotrek ([`bf86d9a`](https://github.com/lotrekagency/camomilla/commit/bf86d9a1134116529454099015e87a19f31292cd))

* Add utility to get content or redirect to the correct language ([`ba303be`](https://github.com/lotrekagency/camomilla/commit/ba303be4c89a603376e6aa861dfcce42e8fb7ccd))

* Add compatibility with Bossanova Angular 8 ([`2c24bc4`](https://github.com/lotrekagency/camomilla/commit/2c24bc4db8bd8275656238bd85f234ebde18966b))

* Add ckeditor for django ([`3f2c4f2`](https://github.com/lotrekagency/camomilla/commit/3f2c4f252c88af788601dd806b52055a5dfb3b6c))

* Fix dependency link ([`f196440`](https://github.com/lotrekagency/camomilla/commit/f196440b586d4fba4b4c101058fc654661774650))

* Fix dependency link ([`40c824a`](https://github.com/lotrekagency/camomilla/commit/40c824a5dbedcbb8297fe2d470be7f51a171541f))

* Fix dependency link ([`e35ba4f`](https://github.com/lotrekagency/camomilla/commit/e35ba4f7694cfe94f463ba518cd9262fc8531ce1))

* Fix setup.py ([`02f423e`](https://github.com/lotrekagency/camomilla/commit/02f423ed15a2d989cd4277520cd6c504ff5ab229))

* Fix dependency link ([`c21edba`](https://github.com/lotrekagency/camomilla/commit/c21edba6217e39941620a17270e92a4079a9399c))

* Fix dependency link ([`87f74b7`](https://github.com/lotrekagency/camomilla/commit/87f74b7866cb0f4f56acf48f2671007a5399212a))

* Fix dependency link ([`391adf1`](https://github.com/lotrekagency/camomilla/commit/391adf198a9ecd3db6d8842d8bf8092acaa0a400))

* Fix dependency link ([`664208c`](https://github.com/lotrekagency/camomilla/commit/664208c03f85f4b3168c546d131abb01909ee859))

* Remove dependency link ([`ec45bf9`](https://github.com/lotrekagency/camomilla/commit/ec45bf971317293757befafe9b7339e2ab37a7d5))

* Fix setup.py ([`8eff9af`](https://github.com/lotrekagency/camomilla/commit/8eff9afb1ab263cf7414ce1459e2a95b11270823))

* Add hvad dependency link ([`2495a2f`](https://github.com/lotrekagency/camomilla/commit/2495a2f4c63a0866cf741ef47b750683a537b7dc))

* Remove useless stuff ([`87c0ccb`](https://github.com/lotrekagency/camomilla/commit/87c0ccb287e1af6d6132e89ac9be20205eb548b3))

* Update README ([`377af1a`](https://github.com/lotrekagency/camomilla/commit/377af1ab4cf734ffcf5b6e5b29895a8a69681894))

* Update libraries ([`79fbf0e`](https://github.com/lotrekagency/camomilla/commit/79fbf0e580ee72e7b6c1719e6ee6a95ba280c404))

* Update libraries ([`ced0916`](https://github.com/lotrekagency/camomilla/commit/ced0916a43275abba805f6e385d4191be36ef035))

* New Camomilla 5 ([`42d52df`](https://github.com/lotrekagency/camomilla/commit/42d52df670cd2acd3d60f2f8a77f17e00eca31da))

* Fix 0023_articletranslation_content_title for any database ([`4a7ef6e`](https://github.com/lotrekagency/camomilla/commit/4a7ef6e3983e0e3a2a724b7bbb7f79934b7ecacd))

* try to save og image from migrations ([`b2a3c54`](https://github.com/lotrekagency/camomilla/commit/b2a3c548b774101c8886c36ada7f7c9acd7bc3ac))

* added sqlparse to requirements due to migration fix ([`ea0d5d2`](https://github.com/lotrekagency/camomilla/commit/ea0d5d24e79fd7c0444f45e9ef61846a70bd14ec))

* fix bad migration ([`78f52bd`](https://github.com/lotrekagency/camomilla/commit/78f52bd218626dbb5f2f9317439a5d2df02e1b45))


## v4.0.0 (2018-12-31)

### Unknown

* Versio 4.0.0 ([`fa534b4`](https://github.com/lotrekagency/camomilla/commit/fa534b4eb83f3ae1e9248db4613015d376d21b03))

* Ignore dist files ([`5802a73`](https://github.com/lotrekagency/camomilla/commit/5802a73815cbd20d08a00aa3cc654734a0edd2ee))

* Remove egg info ([`3075ba9`](https://github.com/lotrekagency/camomilla/commit/3075ba92e0c3790d0fdd118cf844868eab7341b6))

* New package for Camomilla ([`08e115b`](https://github.com/lotrekagency/camomilla/commit/08e115bf16bc7d82733384fe6a752ebabbcf75cd))

* Merge branch &#39;newbossanova&#39; into &#39;master&#39;

Newbossanova

See merge request lotrekdevteam/camomilla/camomilla!12 ([`b108ae9`](https://github.com/lotrekagency/camomilla/commit/b108ae952c4ddcd9d97d03bf0dac356424735806))

* fix bulk delete trashmixin api ([`66ce1f5`](https://github.com/lotrekagency/camomilla/commit/66ce1f5e6bec122c8cc53d67b431aef7ca1040b4))

* fix solutions in product page ([`994307a`](https://github.com/lotrekagency/camomilla/commit/994307ae4a9dd7b9fc90a07ad79a98509bcb2d3d))

* fix camomilla content api ([`21aa7f6`](https://github.com/lotrekagency/camomilla/commit/21aa7f6744bcbc02828d79efb3f7a27409aa700e))

* trash bin support ([`eae164d`](https://github.com/lotrekagency/camomilla/commit/eae164d3331db96686f3c989913956bd8308bbd7))

* update get_seo to use seomixin models ([`2a6b893`](https://github.com/lotrekagency/camomilla/commit/2a6b893eae42df948208897b244193be154802f8))

* clean parser util ([`416057b`](https://github.com/lotrekagency/camomilla/commit/416057b37ad1c34127fddf4afdcb9f55bf0a5983))

* Translations mixins, parsing of multpart and media upload fix ([`db41a7d`](https://github.com/lotrekagency/camomilla/commit/db41a7d820927457e451116b1b651e9cfec0fc94))

* implement bulk delete ([`314affb`](https://github.com/lotrekagency/camomilla/commit/314affb01af92bec4fd096ba729dddbe61a3c666))

* fix get_seo with fallbacks ([`dcf76f2`](https://github.com/lotrekagency/camomilla/commit/dcf76f2198436ea9476e0db606a0b5537c25eb43))

* added get_or_create to get_seo ([`b6cc631`](https://github.com/lotrekagency/camomilla/commit/b6cc631d2e434ad23fd9954a30917961eb7fdee7))

* refactor language management and add translated languages check ([`ee51590`](https://github.com/lotrekagency/camomilla/commit/ee515907abce97a302b7b69c783da65156e4e81d))

* remove patch from media api ([`d142f26`](https://github.com/lotrekagency/camomilla/commit/d142f2676186503769f40a7c42ed80ee112dd8c5))

* try fix cors ([`d7539f2`](https://github.com/lotrekagency/camomilla/commit/d7539f2eb8891b7e58a4d2820464a3038ce185f1))

* add field in api to see models related to some media ([`97ccbdf`](https://github.com/lotrekagency/camomilla/commit/97ccbdf5a192c3ed600c191e04c0fdcbc3b7ace1))

* disable partial update of media ([`1065045`](https://github.com/lotrekagency/camomilla/commit/10650454e11bdec8938bceaaa9d8828ed70c16c7))

* article lockup for api is now id ([`4c1db1f`](https://github.com/lotrekagency/camomilla/commit/4c1db1f1ece2825dac9b7c19229b091bdc41b036))

* fix a view and forgotten migration ([`756aa05`](https://github.com/lotrekagency/camomilla/commit/756aa05f42a5bc555acf91a37f9714008d21d64f))

* get translate content in pages ([`d198a79`](https://github.com/lotrekagency/camomilla/commit/d198a79ece69fdc5030ffdb4869138ac52ad4bcc))

* add planned choice to articles ([`fa58b3d`](https://github.com/lotrekagency/camomilla/commit/fa58b3d691452d00a6283af7572978b35d42abef))

* added article title not seo ([`34cf1dc`](https://github.com/lotrekagency/camomilla/commit/34cf1dcf5613d874cf2b95672136cbf5def05373))

* og_image is now a media field but we lose old images ([`72f170e`](https://github.com/lotrekagency/camomilla/commit/72f170ee638f50dcd1679889c77fcd6b22219f04))

* wip ([`0b027b1`](https://github.com/lotrekagency/camomilla/commit/0b027b1735ad784c657443f3d1ad5551897d9135))

* better queryset selector for language ([`9615552`](https://github.com/lotrekagency/camomilla/commit/961555240cd0358076acfb4848b2e04804c2aaa8))

* remove validator and leave integrity error ([`f84de8a`](https://github.com/lotrekagency/camomilla/commit/f84de8a4f4065987f3d626e30e618111be5878b5))

* fix language api ([`1c205f4`](https://github.com/lotrekagency/camomilla/commit/1c205f489dbc8263805c2629528d2c8dba9d796f))

* article language fallback queriset wip ([`e10a18c`](https://github.com/lotrekagency/camomilla/commit/e10a18c8fd5d71eb79f8a7fd0386e0617ef9f808))

* fix unique together validation ([`9cc8ae8`](https://github.com/lotrekagency/camomilla/commit/9cc8ae885bf5009c78a6197ec62bab9705ddd3ea))

* fix operations for sortedm2m and mediasortedm2m ([`d65fb16`](https://github.com/lotrekagency/camomilla/commit/d65fb163db318ca4c8c1d57f5b3c2e6e7b9e77b4))

* fix error in sortedm2m and mediasortedm2m uploading files ([`eb5a596`](https://github.com/lotrekagency/camomilla/commit/eb5a5964055a4b41b207dc76ea7f8abb6b146d82))

* Fix tuple error ([`0c8c23f`](https://github.com/lotrekagency/camomilla/commit/0c8c23f40201a5d325ad5e88897cc6482c3ddb50))

* New awesome feature for micro-services ([`7bdf325`](https://github.com/lotrekagency/camomilla/commit/7bdf325552aaaaa87af5eb9b364b7a83b036a7f4))

* Get or create ([`fa106da`](https://github.com/lotrekagency/camomilla/commit/fa106dacbdee3c2f495e7c82b29243a54190a87b))

* Hello new base serializer 🎅🏻 ([`822aee0`](https://github.com/lotrekagency/camomilla/commit/822aee03f2a08e44003a4cd19949ab8c09220ace))

* add user image on user serializer ([`c0fdaeb`](https://github.com/lotrekagency/camomilla/commit/c0fdaeb9a4b66c2b2fca15e3544605c8356d4a5a))

* added api for current user ([`b720d2e`](https://github.com/lotrekagency/camomilla/commit/b720d2e99f0f461ae151d34c33bf7fdbdafd2ede))

* No more author in Contents ([`50471c8`](https://github.com/lotrekagency/camomilla/commit/50471c823a83adb65446ad4957923c6f2e03a55a))

* Fixes on serializers ([`c1389d1`](https://github.com/lotrekagency/camomilla/commit/c1389d1259de746bc02b0f48b422dcc4f34682af))

* Fix migrations ([`f120a96`](https://github.com/lotrekagency/camomilla/commit/f120a9699395cfe5bd4c0861f531424f244bc425))

* Media folder migrations ([`7c8b7db`](https://github.com/lotrekagency/camomilla/commit/7c8b7dbd3e5c86363b101c44eb183e0c3b2dd4b7))

* Page on Admin.py ([`ba907f2`](https://github.com/lotrekagency/camomilla/commit/ba907f218277177a792c1c7066220a6ab0ea557d))

* Media folders endpoint ([`fe619a0`](https://github.com/lotrekagency/camomilla/commit/fe619a0710aec9f55cda428d89489672407d9776))

* Og description is now a text field ([`1955503`](https://github.com/lotrekagency/camomilla/commit/19555038ba50b31b67ca1386dbdab71cb25841ba))

* Ignore mo ([`145075f`](https://github.com/lotrekagency/camomilla/commit/145075f75f7daea032b9598ef31cedba2a98312c))

* Minfixes on serializers ([`2a7f111`](https://github.com/lotrekagency/camomilla/commit/2a7f11132c521e91ddde035bc87e2b0daea4bfee))

* Refactoring on Article ([`6c9b400`](https://github.com/lotrekagency/camomilla/commit/6c9b400a445e4444ac74f0f6189aa4bbd479c3fa))

* SitemapUrl is now (finally) Page ([`e8ebaa5`](https://github.com/lotrekagency/camomilla/commit/e8ebaa541817a0eb711ecb009dd0b6cf6fd9a3b9))

* Fix cache middleware ([`d5f401b`](https://github.com/lotrekagency/camomilla/commit/d5f401b0e9ff6424223fbd8eb0409bbbac2911ea))

* Update hvad ([`8c1b5d7`](https://github.com/lotrekagency/camomilla/commit/8c1b5d7fc3d71dfc21bf057bceff6a429e2dc8a7))

* Better filter for contents ([`71924c0`](https://github.com/lotrekagency/camomilla/commit/71924c0efdba8a524723833fa07b7fdee17efc6f))

* Add templatetags ([`fb857fa`](https://github.com/lotrekagency/camomilla/commit/fb857fa33efb62d8271b07ca20dce6e49e86bd98))

* Add date to show ([`db007e8`](https://github.com/lotrekagency/camomilla/commit/db007e8e81ea5fd4cf42b5dd254f067bfbc9514d))

* Better cache management ([`7bba434`](https://github.com/lotrekagency/camomilla/commit/7bba434eeb1552cf408655be7bc09a1801ad6d5f))

* Minfix on SEO utils
now permalink is always request.path ([`ab4e2d5`](https://github.com/lotrekagency/camomilla/commit/ab4e2d5a0e13a9f8b93508cb1fc5adb231e6563f))

* Fix thumb_url assignment ([`672d633`](https://github.com/lotrekagency/camomilla/commit/672d6335cee193bfd8c9cd97b792acdd732c021e))

* Remove useless migration ([`a99bc50`](https://github.com/lotrekagency/camomilla/commit/a99bc50577be4bbf3ba8ab83c0219f14169e44e9))

* Add remaining migration ([`38523d8`](https://github.com/lotrekagency/camomilla/commit/38523d8319045d63e19d1ee18aa68f8cd1d597ac))

* align ([`e1005a3`](https://github.com/lotrekagency/camomilla/commit/e1005a32dd61d5b228c00fab2b633e59bc458d89))

* Useless migration ([`b38d7c3`](https://github.com/lotrekagency/camomilla/commit/b38d7c3855c75bf942f2846ab97ef6f37f682074))

* Do not use default url prefix ([`7240792`](https://github.com/lotrekagency/camomilla/commit/72407928b38942771cc2f12bc9142694bcbb2dff))

* update labels ([`ce15ed4`](https://github.com/lotrekagency/camomilla/commit/ce15ed432f371b751223c210bff500c0cd03e857))

* Remove files on media delete ([`ce6cb48`](https://github.com/lotrekagency/camomilla/commit/ce6cb480fce9afa5c6707c4545a434aacdadc51c))

* Save optimized images ([`4ed9466`](https://github.com/lotrekagency/camomilla/commit/4ed94667829c8c30ed7d0719db806f66f2412fcd))

* Generate thumbnail on post save ([`d6847cc`](https://github.com/lotrekagency/camomilla/commit/d6847cc4f3e397db596d4ed2385fa9575f6aed8c))

* Generate thumbnail on post save ([`ae773d0`](https://github.com/lotrekagency/camomilla/commit/ae773d06909d6b9a066a08cfb053154d606abd6c))

* Async optimization ([`7743a79`](https://github.com/lotrekagency/camomilla/commit/7743a79cc94849b9fa678db9ded020df95e805c2))

* Use media root ([`e39f6f3`](https://github.com/lotrekagency/camomilla/commit/e39f6f3b77211a58d916b1864ba4beaf919f97d0))

* Optimize on save ([`731ef8d`](https://github.com/lotrekagency/camomilla/commit/731ef8d621733857e41cd47fc43a39c06d1ee43d))

* Add media optimization ([`e480526`](https://github.com/lotrekagency/camomilla/commit/e480526f5c0453d97938b305f6ace1ac0bfb5d1d))

* Fix regeneration thumbnails ([`142846f`](https://github.com/lotrekagency/camomilla/commit/142846f1caa4b84a56aef59a2377ceb12bc5f892))

* Remove print ([`de4524f`](https://github.com/lotrekagency/camomilla/commit/de4524ff5382f55f8fd3c97a886cab9a7a80e45d))

* Improvements on thumbnail generation ([`9bb823f`](https://github.com/lotrekagency/camomilla/commit/9bb823f559f95769f1f1edc8b013cc271ef7abb5))

* Og_image in sitemap serializer
Media objects are now ordered by &#39;create&#39; datefield ([`b739fa2`](https://github.com/lotrekagency/camomilla/commit/b739fa265a3ab4b6fd7b6b3d259a5f7b81d68c6f))

* Merge branch &#39;master&#39; of bitbucket.org:lotrek-tea/camomilla ([`52f4c00`](https://github.com/lotrekagency/camomilla/commit/52f4c00125c2df60aa3e4c920a7f32d22018d8f2))

* Description is now on compactSerializers ([`4bd69d3`](https://github.com/lotrekagency/camomilla/commit/4bd69d3c61e75280efa22043184eae5a2f36d286))

* Only superuser can access to all users ([`3674998`](https://github.com/lotrekagency/camomilla/commit/367499854d08bc7536b3ca22862c06533a10f95c))

* Fix statics and templates ([`0ca7b27`](https://github.com/lotrekagency/camomilla/commit/0ca7b2798fa4c6a5b25ad9cb26e88b50fc19cc52))

* Fix on new widgets ([`7fa9f71`](https://github.com/lotrekagency/camomilla/commit/7fa9f71b33e73e0d5b9e40bbe914f1f245230972))

* New style and new widgets ([`0d9e0fb`](https://github.com/lotrekagency/camomilla/commit/0d9e0fbfe28b1795260939c6eca692250cd22636))

* Media Model now has Description field ([`e8402e5`](https://github.com/lotrekagency/camomilla/commit/e8402e59d32d098f485c6e2e0d08b640e611adea))

* Fix user creation ([`17931e5`](https://github.com/lotrekagency/camomilla/commit/17931e5c773615e2ee746dc30179656897144014))

* Minfix on Filter in Views ([`d70f18d`](https://github.com/lotrekagency/camomilla/commit/d70f18d03235ccf7c897eddd2819125b76b51fcf))

* Add search for images ([`1de7de4`](https://github.com/lotrekagency/camomilla/commit/1de7de4c228895fb11cf9489e2ec8fe9e9dc91db))

* Fix admin ([`18a9ad8`](https://github.com/lotrekagency/camomilla/commit/18a9ad8346f566c352ac15012cded89782ce5f0f))

* New repr for media ([`160a990`](https://github.com/lotrekagency/camomilla/commit/160a990790b1a8fc262676ef374bba7bc7949c52))

* Add style ([`a78318b`](https://github.com/lotrekagency/camomilla/commit/a78318b5d9906fb4283d6d507d61a2ce7212ca6f))

* Fix multiple media select widgets in the page ([`c2dd4e9`](https://github.com/lotrekagency/camomilla/commit/c2dd4e9f131c78a3e35f3832adc7ca81b59cd350))

* Fix unselected media for media selector ([`9f11b51`](https://github.com/lotrekagency/camomilla/commit/9f11b511b2c420cc44da2af63a7b1217fb2f1366))

* New dynamic media select ([`336f912`](https://github.com/lotrekagency/camomilla/commit/336f912e3aa8615d1909b408cf8cc5d66ab14605))

* remove of tests.py that block global test run ([`bdf9eca`](https://github.com/lotrekagency/camomilla/commit/bdf9eca743548943a319a7c8a3d9b350a8b8834d))

* Fix Articles fields ([`d8a1746`](https://github.com/lotrekagency/camomilla/commit/d8a1746d0c73e4e2872618b3ee15d601ff185768))

* Add redactor ([`36fb4a8`](https://github.com/lotrekagency/camomilla/commit/36fb4a8e558402676c0aa13c74e94ecebfc5f117))

* Updated Viewset of SitemapUrl
Now you can read with CamomillaBasePermission
You can filter your queryset by permalink ([`00f35fb`](https://github.com/lotrekagency/camomilla/commit/00f35fb4ba01198bc6d015f7019edf0770b5f336))

* More work on slug ([`ce3a803`](https://github.com/lotrekagency/camomilla/commit/ce3a8039d4159d1bed604be7cc19be5548bb8a99))

* Add get_article_with_seo ([`9e4117a`](https://github.com/lotrekagency/camomilla/commit/9e4117ac8220511129527eb72ed2f37fc1e62078))

* Add identifier for articles ([`9c4d585`](https://github.com/lotrekagency/camomilla/commit/9c4d585233e1bc13d719bc6af4779eec82340c8a))

* More tests on utils ([`3e28f70`](https://github.com/lotrekagency/camomilla/commit/3e28f70d90c31146cc08c30e666b338d31467325))

* Add tests ([`81c8bc4`](https://github.com/lotrekagency/camomilla/commit/81c8bc44b4a5ebf03026c61ad520beaab8b19769))

* Permalink no more mandatory ([`3905a12`](https://github.com/lotrekagency/camomilla/commit/3905a1243f31448591f1bf16b0f17cedb77d478f))

* Set null instead of cascade ([`41216bb`](https://github.com/lotrekagency/camomilla/commit/41216bba6637e5aab7bc3684ef9ea1b0f46ee459))

* Add thumbnail ([`09c1bdc`](https://github.com/lotrekagency/camomilla/commit/09c1bdcbb3bbf41f59d6285f7dc875c1856b66f4))

* Fix thumbnail generation ([`31b21bd`](https://github.com/lotrekagency/camomilla/commit/31b21bd25a2d4f6ff345db4f0561b71dbd532e22))

* Check if file exists before opening ([`30c2abc`](https://github.com/lotrekagency/camomilla/commit/30c2abc8858dae7055d818d09921ecdc0fe7b72a))

* Add command for thumbnail regeneration ([`4a1c4fe`](https://github.com/lotrekagency/camomilla/commit/4a1c4fe8c97035f84b5698eb18f9f0ceafa1578a))

* Save and generate thumbnails in media ([`a058440`](https://github.com/lotrekagency/camomilla/commit/a0584409f8f84d100d94809188f21b545772e3c1))

* RGB conversion hack disabled at the moment ([`5e1b656`](https://github.com/lotrekagency/camomilla/commit/5e1b6567135a859af083826684a78a04a2b725d9))

* Change defaults ([`484be33`](https://github.com/lotrekagency/camomilla/commit/484be3379c9b4cbabadd8c702ae1a4fcd3a93895))

* Add custom widgets for media selection ([`087e000`](https://github.com/lotrekagency/camomilla/commit/087e0000eb55b9f795917990521dabaa1c756469))

* Updated SEO Utils Engine
Hotfix for multilanguage site, and custom SitemapUrl class ([`ab69333`](https://github.com/lotrekagency/camomilla/commit/ab69333d9be5a2c55cf920a5b946158889ad16dd))

* Add new requirements.txt ([`9a4c46b`](https://github.com/lotrekagency/camomilla/commit/9a4c46b56293a39ba39eea54383a3d5b4869a179))

* Keep only the app in this repo ([`122b01e`](https://github.com/lotrekagency/camomilla/commit/122b01e0a422818b861d8ce836e1735d6012bc5e))

* Update tags ([`17a30ed`](https://github.com/lotrekagency/camomilla/commit/17a30edc5aaf63e47a58c3ffcb5da13a807f125e))

* Fix import settings ([`112d5a3`](https://github.com/lotrekagency/camomilla/commit/112d5a3a231854ed59052339338195c07cd4769c))

* Og_image is an image field ([`e1070c9`](https://github.com/lotrekagency/camomilla/commit/e1070c9834f58e8dc667089d5301ee4075eefb19))

* Add get_seo utility (thanks Busi) ([`e5463c4`](https://github.com/lotrekagency/camomilla/commit/e5463c46067568537a4e6401a11c4032466ddf05))

* Add missing migrations ([`e81e2ca`](https://github.com/lotrekagency/camomilla/commit/e81e2ca92a58845736b028d49a1c3a2d0d8f1f61))

* Add cache middleware ([`fcada75`](https://github.com/lotrekagency/camomilla/commit/fcada75a9a5f037f034e80e76e0b3cb9d76fcdc1))

* Merged in hotfix/renaming-classes (pull request #9)

Renamed Class ([`a06a4e7`](https://github.com/lotrekagency/camomilla/commit/a06a4e75de4f61db752508c1703c8ef0cdc589cb))

* [Rename] ExpandeNdArticleSerializer to ExpandedArticleSerializer ([`6c17aea`](https://github.com/lotrekagency/camomilla/commit/6c17aea2e1b31c9fbb61105ca33a4c076629a659))

* Fix typo ([`ca90577`](https://github.com/lotrekagency/camomilla/commit/ca90577e43ccbc178ca0286d9a9c860845bb2df5))

* Add new constraints for identifier ([`fed1d32`](https://github.com/lotrekagency/camomilla/commit/fed1d3264875e22864f110d6d4dc471aa7f391a9))

* Contents retrieved by unique key ([`7c66627`](https://github.com/lotrekagency/camomilla/commit/7c6662713324bcd6d41713bd753268624f8bb2a8))

* Fix thumb conversion ([`6a08f60`](https://github.com/lotrekagency/camomilla/commit/6a08f60753383defb35a324cf5f4ce099fe2a3e6))

* URL_PREFIX is not mandatory ([`77be0b3`](https://github.com/lotrekagency/camomilla/commit/77be0b39bce62e8e7d85e3f2d34410b490ec37a8))

* Add some notes about default settings ([`408e3e2`](https://github.com/lotrekagency/camomilla/commit/408e3e2e558bfcae84a98ea4a83b42298dcb5305))

* Raise an ex if AUTH_USER_MODEL is not defined ([`0d1b69a`](https://github.com/lotrekagency/camomilla/commit/0d1b69aec66fe1fb84fb5e7d76be13e32d504f79))

* Fix defaults ([`d10edcf`](https://github.com/lotrekagency/camomilla/commit/d10edcf402a99a615ce4c623551c4939e65fb4a0))

* Camomilla defaults FTW 🤘🏻 ([`cdeaf41`](https://github.com/lotrekagency/camomilla/commit/cdeaf4136a1ed6a02fed93673f8743e27ef930d7))

* Pass ‘reset’ to reset to origin/master ([`d3ec377`](https://github.com/lotrekagency/camomilla/commit/d3ec37782f43ab686208f2fda43702dc523b7edf))

* New robust deploy script ([`1597fa6`](https://github.com/lotrekagency/camomilla/commit/1597fa6031a551bbaa5099fd741a82d34eded003))

* Add defaults ([`cca7668`](https://github.com/lotrekagency/camomilla/commit/cca766874f33bb42a25c041e80479e7113ee18f9))

* Merged in minoLotrek/bitbucketpipelinesyml-created-online-wit-1481293746573 (pull request #8)

bitbucket-pipelines.yml created online with Bitbucket ([`e655cdb`](https://github.com/lotrekagency/camomilla/commit/e655cdb93fccf99dfb3b55e25e099570c6972667))

* bitbucket-pipelines.yml created online with Bitbucket ([`0af58d9`](https://github.com/lotrekagency/camomilla/commit/0af58d96523ada7eb24f6132e3c5b9038b2ada00))

* Merged in feature/new_user_profile (pull request #7)

New user profile ([`253d44f`](https://github.com/lotrekagency/camomilla/commit/253d44faebaa22cbf4e92057d869d90f77c38e09))

* Remove base user ([`3f5f057`](https://github.com/lotrekagency/camomilla/commit/3f5f05781767f5f74799aa97d9c1b6b6be573a6e))

* More on user customisation ([`d9d4f30`](https://github.com/lotrekagency/camomilla/commit/d9d4f304afa98dc81d6662b105b3f973d9f3eefe))

* Fix migrations again ([`fc3f56a`](https://github.com/lotrekagency/camomilla/commit/fc3f56af240e97ef6dc2bb8be209eeaa6875209d))

* Reset migrations ([`39b8d54`](https://github.com/lotrekagency/camomilla/commit/39b8d54aa2cc573d6b62c66204d0456bc14099d3))

* New user profile management ([`f5fb19b`](https://github.com/lotrekagency/camomilla/commit/f5fb19b5162a55324a9a80e2f1701e30554095e2))

* Add read permissions (no way for clients to break our balls 🖕🏻) ([`5e8afd3`](https://github.com/lotrekagency/camomilla/commit/5e8afd3c84baf5404a271fd4f89911d96cd3e506))

* Merged in feature/newcontents (pull request #5)

[WIP] New contents with a page ([`c15e886`](https://github.com/lotrekagency/camomilla/commit/c15e886e3464e212395aa68a4bff573d0c39df8a))

* Merge remote-tracking branch &#39;origin/master&#39; into feature/newcontents ([`9a940f1`](https://github.com/lotrekagency/camomilla/commit/9a940f1a19ba319340d67f5848be228e613a660a))

* Merged in feature/custompermissions (pull request #4)

[WIP] Custom permissions ([`b2f2165`](https://github.com/lotrekagency/camomilla/commit/b2f21650c124c2ab2648d13d96d0d109a08404ba))

* Merged in feature/security_improvements_and_deploy (pull request #6)

New deploy with security improvements ([`48791fa`](https://github.com/lotrekagency/camomilla/commit/48791fa4b5675c69e1304e6738737abdb52e7073))

* Add token and user permissions ([`9dd0d88`](https://github.com/lotrekagency/camomilla/commit/9dd0d88bedaa574ea8516089db51dc201c21137e))

* Sitemap as pages ([`23a785b`](https://github.com/lotrekagency/camomilla/commit/23a785ba49d8a771042d93a6892592e20f0b10cf))

* Let Gunicorn running with a socket 🎉 ([`dd7dae0`](https://github.com/lotrekagency/camomilla/commit/dd7dae0e074869cc6f2ec7bc8243d559abc34deb))

* Return permissions on profile get ([`d836d93`](https://github.com/lotrekagency/camomilla/commit/d836d93c195b6c77d2b9975626548d93bd66c64c))

* Auto set only camomilla permissions ([`67c2844`](https://github.com/lotrekagency/camomilla/commit/67c284458fe8030d44100e04ad59b87ef6a75044))

* Add url fields for models ([`6ecc3ac`](https://github.com/lotrekagency/camomilla/commit/6ecc3ac009a88b12ae264dba7184838c95371dda))

* New media creation ([`9c59e35`](https://github.com/lotrekagency/camomilla/commit/9c59e35e39ad1062b7b6d1580236ecb0416d967d))

* Install setproctitle 🎉 ([`c8a8d8b`](https://github.com/lotrekagency/camomilla/commit/c8a8d8b7fd1179c4ba6353ddb18ddf46282f4f3d))

* Kill and run unique gunicorn process ([`6afd646`](https://github.com/lotrekagency/camomilla/commit/6afd646faa42560185604dfaadea2456fdf85e25))

* Some fixes on internal admin ([`79eeaea`](https://github.com/lotrekagency/camomilla/commit/79eeaea9a2d4859b94d4a468d6a0f26673cb0f44))

* Restore old deploy script ([`a00d6a3`](https://github.com/lotrekagency/camomilla/commit/a00d6a3c2045604af0a42052b236e97c7459c1b6))

* New deploy with security improvements ([`84288e9`](https://github.com/lotrekagency/camomilla/commit/84288e9beeb93ea53c3a1593ffe4a5064e9033a8))

* Use only camomilla&#39;s categories ([`23f3ec2`](https://github.com/lotrekagency/camomilla/commit/23f3ec2c7e0dd115b7254e5fb2bf1634cb3391af))

* Add pages ([`d76545a`](https://github.com/lotrekagency/camomilla/commit/d76545ac7dab5f2706cc175930d3b5cec534841a))

* Add some deploy notes ([`a76e633`](https://github.com/lotrekagency/camomilla/commit/a76e633d21e2c007c9b9a1410e06ab1a62b2aa16))

* Add deploy info ([`8ba4efc`](https://github.com/lotrekagency/camomilla/commit/8ba4efcf762a9679baf4d6906bd1697ee4d2d5b9))

* First changes for translatable fields (hvad hack in README) ([`15fee75`](https://github.com/lotrekagency/camomilla/commit/15fee7597da73d8b9db2f87cc506f272a90d579a))

* Add backend for creating users and set permissions ([`e92f282`](https://github.com/lotrekagency/camomilla/commit/e92f282cc84ff8c496c66fad6e948f4dc867b64b))

* Check custom permissions in Camomilla permission class ([`ee42055`](https://github.com/lotrekagency/camomilla/commit/ee4205596d4a7ff33e819137bc8dd41f8c327830))

* Merged in fix/abstractArticle (pull request #3)

Support for inheritance. ([`a01f60f`](https://github.com/lotrekagency/camomilla/commit/a01f60ff398b909462fef70f23b629c251b5a59a))

* Make views more abstract ([`620fb1a`](https://github.com/lotrekagency/camomilla/commit/620fb1a7f097f1e9eaecae69ba6da7c2f65fd873))

* Cleaning code ([`6bc771f`](https://github.com/lotrekagency/camomilla/commit/6bc771fcaf94cbfd2e42e4810de967f90152dcb5))

* All Main-Models of Camomilla (no media) now are abstract ([`430e6b7`](https://github.com/lotrekagency/camomilla/commit/430e6b722978e21a1e938c8292d2e8ae2330944f))

* Update of gitignore ([`8d35716`](https://github.com/lotrekagency/camomilla/commit/8d357166f0c2e75f810683e0929d32edf9097182))

* Support for inheritance of Article.
Dynamic Serializer.
Redefined the correlations with classes(FK), inheritance support. ([`a2983ba`](https://github.com/lotrekagency/camomilla/commit/a2983bae82897cc8a304ed8afd5a2c5b7c59f231))

* Add level 3 if user is superuser ([`ed38b9f`](https://github.com/lotrekagency/camomilla/commit/ed38b9fb5e3ac757946f598b9931b964b92e8b16))

* Better names for admin objects ([`8d76858`](https://github.com/lotrekagency/camomilla/commit/8d768587ec0899b94c106dd2876dc98ad0a264f8))

* More on settings ([`f03d651`](https://github.com/lotrekagency/camomilla/commit/f03d65180b07ecbd481df2aae464b987a7160fc1))

* Fix post on upload ([`33dcfc8`](https://github.com/lotrekagency/camomilla/commit/33dcfc87d0928c1028db3253c67e59eda84eaf7b))

* Do not accept requests if user is not authenticated ([`1db4600`](https://github.com/lotrekagency/camomilla/commit/1db460011f39356f00805eb967b532e696bb615f))

* Tags and categories may be blank ([`5639aed`](https://github.com/lotrekagency/camomilla/commit/5639aed548295be8d2121c5847188dd18b1275d7))

* Remove useless plugin ([`b04c8a4`](https://github.com/lotrekagency/camomilla/commit/b04c8a4fddb839db9714834db326a36c1ce8f08a))

* Merged in feature/check_permissions (pull request #2)

Feature/check permissions ([`1f6a5ac`](https://github.com/lotrekagency/camomilla/commit/1f6a5ac084472854de790eefdc9d11461bff3c7d))

* Merged in feature/translatable_permalink (pull request #1)

Feature/translatable permalink and other fixes ([`fb2d1c1`](https://github.com/lotrekagency/camomilla/commit/fb2d1c1ca039291b93a8220c45dd8a647da8fa14))

* Update README ([`9e26e7b`](https://github.com/lotrekagency/camomilla/commit/9e26e7b97828e0b99139a3488d87be576a7dd606))

* Remove useless plugin url ([`2bf1869`](https://github.com/lotrekagency/camomilla/commit/2bf1869fce14e8fef0cda365bb86e9fca850e01d))

* Fix README ([`119a3c9`](https://github.com/lotrekagency/camomilla/commit/119a3c9fe6c91d2ecf4c7495abaaf22139589567))

* Fix warnings ([`2b2fed9`](https://github.com/lotrekagency/camomilla/commit/2b2fed905099b9b4b3102855cdc058e9151f1fe9))

* Use right language in case of PUT/PATCH ([`ea7653b`](https://github.com/lotrekagency/camomilla/commit/ea7653bf3e971817990931fd1868025416e59aa0))

* Add related name for User ([`8766e89`](https://github.com/lotrekagency/camomilla/commit/8766e89d138df691cbc048e385c97be3d6eca29d))

* Add base permissions for Camomilla ([`c1ecaf4`](https://github.com/lotrekagency/camomilla/commit/c1ecaf4e0501079a91bdd0a693a620911a9dab1f))

* First attempt to make translatable permalink working (refactoring needed!) 🎉 ([`4e71e5f`](https://github.com/lotrekagency/camomilla/commit/4e71e5f7849e5a5cbfa7da8bab355b97bbf51459))

* New highlight image ([`96fc296`](https://github.com/lotrekagency/camomilla/commit/96fc2962a140eb56efce2538bf23f161d6ca314a))

* New images file size calculation ([`aef72a7`](https://github.com/lotrekagency/camomilla/commit/aef72a73c5acf72f3126be9c430acf25fb0ac7f2))

* Fix thumb creation ([`4e0c18e`](https://github.com/lotrekagency/camomilla/commit/4e0c18e5eebe604a03ba2ea9ce19945e685f843c))

* Fix retrive article with the correct language ([`f5b2132`](https://github.com/lotrekagency/camomilla/commit/f5b21329ccdab7b6a5f86c71de13e1465ef078ea))

* Add plugin support ([`6bfbdbf`](https://github.com/lotrekagency/camomilla/commit/6bfbdbf5f683252aa5e84ec98ef19247c2a19f3a))

* Big refactoring (+ auto create profiles after user creation) ([`c77633a`](https://github.com/lotrekagency/camomilla/commit/c77633a8d13b111bb1f1023108a0f2faad4b1dfd))

* Add user profiles serialisation ([`a16135d`](https://github.com/lotrekagency/camomilla/commit/a16135de0abb9218b234a02719df8e9e9ce28e20))

* Add thumbnails support ([`54ba655`](https://github.com/lotrekagency/camomilla/commit/54ba6552e89195d9da2215177a517ef4642a01a6))

* Fallback for tags and categories ([`726e320`](https://github.com/lotrekagency/camomilla/commit/726e320a4f227b8af3333e9ac1054c60b651cb77))

* Translate support for contents ([`e8a34b9`](https://github.com/lotrekagency/camomilla/commit/e8a34b9c8e3f6c8adc019e72b14dbfd1c1c4710b))

* Fix languages ([`ca41fac`](https://github.com/lotrekagency/camomilla/commit/ca41facecb4cd1c0196ca2711e8beab087547f93))

* Remove useless den settings app ([`f6ef2d0`](https://github.com/lotrekagency/camomilla/commit/f6ef2d08909ecc0df1dbe592b1f50cb6b8098aee))

* Raw languages API exposition ([`c0d040d`](https://github.com/lotrekagency/camomilla/commit/c0d040dbf078eb293b3801a8f3be76d65c109e65))

* Media refactoring ([`5ad7c1b`](https://github.com/lotrekagency/camomilla/commit/5ad7c1bf42fe9cec3524b54e2bbce3080b588b3b))

* Add multilanguage support ([`de9cd0a`](https://github.com/lotrekagency/camomilla/commit/de9cd0a4795f62f20cf793d3852b0bc346381e75))

* Get additional info with the token ([`9f6caa7`](https://github.com/lotrekagency/camomilla/commit/9f6caa761c5aa6320f43757561b5bb1b6965454c))

* Minfixes ([`5d452d2`](https://github.com/lotrekagency/camomilla/commit/5d452d2be505e688cec8990215cf1c7169074419))

* Add sitemap ([`638038c`](https://github.com/lotrekagency/camomilla/commit/638038c2f66d64b752fc1ae1ceb91bfee098df44))

* Add media ([`df4f82c`](https://github.com/lotrekagency/camomilla/commit/df4f82ccb40ebb62028491b0324ac33686550d48))

* Add contents ([`c27222b`](https://github.com/lotrekagency/camomilla/commit/c27222bf53413dccd725b9d1e7d34447f39b9689))

* Unique values for tags and categories ([`674e65a`](https://github.com/lotrekagency/camomilla/commit/674e65a3e5151c7ac6403c8715ab7abbf6a21fdf))

* Update view ([`5ef7d6c`](https://github.com/lotrekagency/camomilla/commit/5ef7d6cc74203e9af47fcecd251fe9dc217ca1a1))

* Tags and Categories are not mandatory ([`e1b6943`](https://github.com/lotrekagency/camomilla/commit/e1b6943a86cbee9fd2210762c1f294b3382c2278))

* More on articles ([`f7a971b`](https://github.com/lotrekagency/camomilla/commit/f7a971b386debf657f716477f85ba271b4fe51c0))

* Add admin for models ([`714b464`](https://github.com/lotrekagency/camomilla/commit/714b4648498e90f4f2f3c69e4fae012acd9dd67e))

* Set up database ([`50fb87d`](https://github.com/lotrekagency/camomilla/commit/50fb87d720c0f2b696547efbcce61f3cac80d3af))

* First import ([`7fbc2d7`](https://github.com/lotrekagency/camomilla/commit/7fbc2d76c8bd6ea5c04b45fc5de9ee21de290401))
