# Changelog

<!--next-version-placeholder-->

## v6.0.0-beta.1 (2023-07-31)
### Feature
* Added autoptimized storage for media files ([`93e02a1`](https://github.com/lotrekagency/camomilla/commit/93e02a1c189da6520d80947c53f3ae741523668c))
* Added page routerlink to have an exact reverse match of permalinks ([`d50396e`](https://github.com/lotrekagency/camomilla/commit/d50396e41d22ff11ba66e7c36061f2cd16ac2204))
* Translatavle template_data ([`7d25ef7`](https://github.com/lotrekagency/camomilla/commit/7d25ef7250375579971530574d91a82f83b4b864))
* Added template_data to abstract page" ([`07bb9a1`](https://github.com/lotrekagency/camomilla/commit/07bb9a151311ab1917a727b12d5fb21e94609204))
* Added camomilla settings to change defatult many behaviours ([`53be09c`](https://github.com/lotrekagency/camomilla/commit/53be09cc7c265d5f1ab5007b35115a1d4da9f099))
* Added page meta inheritance ([`69f93a3`](https://github.com/lotrekagency/camomilla/commit/69f93a33d34ac998968a1f8887e24342cc99f6f4))
* Added the possibility to select menu template to render ([`bd8b05f`](https://github.com/lotrekagency/camomilla/commit/bd8b05f8e9e0165e723c5d90dbad3d49239f00df))
* Added get_context to page model ([`c9645ef`](https://github.com/lotrekagency/camomilla/commit/c9645efa722bcb0397b9facb44794a4d52815f32))
* Added serializers for structured data ([`325ce53`](https://github.com/lotrekagency/camomilla/commit/325ce535f32605014ccbd3fe3447674d328ddbd1))
* **structured:** Added cache to StructuredJSONField 🚀 ([`e3d0d6a`](https://github.com/lotrekagency/camomilla/commit/e3d0d6aabaf943810d0662090a7a3c6cec1c7fd4))
* **structured:** Added cache for listfields ([`d70f35d`](https://github.com/lotrekagency/camomilla/commit/d70f35dfbb5e1a7fbf3c27a0ce7e53dec52677b8))
* **model_api.py:** Created basic register decorator ([`e62bd37`](https://github.com/lotrekagency/camomilla/commit/e62bd37cc5d0f5d3b4f231f1d8b1a52f1294db09))
* Removed migrations and added MIGRATION_MODULES setting injection ([`5e770f3`](https://github.com/lotrekagency/camomilla/commit/5e770f3f367f2e404b56c8c5d4469b816218b901))
* Added shortcuts to render menus ([`6f23fe9`](https://github.com/lotrekagency/camomilla/commit/6f23fe9f8cb100a95d5fdbae05ab9af8881a555d))
* Added StructuredJSONField descriptor ([`651b134`](https://github.com/lotrekagency/camomilla/commit/651b134f408885f3746a7a0b782d68f8dbd66c06))
* Added StructuredJSONField ([`de3bb6d`](https://github.com/lotrekagency/camomilla/commit/de3bb6dbf17e7d3bf8dca126d2cbef5664be6f99))
* Added dynamic_pages_urls and template management ([`1620d0a`](https://github.com/lotrekagency/camomilla/commit/1620d0a74fe3609c133237bb5fbb8ae2cc116948))
* Added class methods to Abstractpage to facilitate camomilla upgrade from old versions ([`4d4b381`](https://github.com/lotrekagency/camomilla/commit/4d4b381c56bfa16e2123ee08f47c18b6a3a6d3a4))
* Added some translations utils ([`7185ae1`](https://github.com/lotrekagency/camomilla/commit/7185ae17868a7826369790bbbf4f1230bd7f4a5d))
* Add djsuperadmin urls if present ([`81ec4e8`](https://github.com/lotrekagency/camomilla/commit/81ec4e8439649f7dddba8a3088a956a6b2f5c851))
* Default translate menu nodes ([`a051ae9`](https://github.com/lotrekagency/camomilla/commit/a051ae97838a5e6a3eca346facb1d1c06969031b))
* Added menù model and serializers ([`cc902ea`](https://github.com/lotrekagency/camomilla/commit/cc902eab73b198932fe00afd66e3eeb0e48afd79))
* Added urlnode autogeneration and slug validator ([`12cd811`](https://github.com/lotrekagency/camomilla/commit/12cd8111a4f1deefcb65aa346b893930978d1539))
* New urlnode structure for pages ([`2576520`](https://github.com/lotrekagency/camomilla/commit/2576520cd37f9a7a415da941e5c7260e30f7e410))
* Added way back migration helper to return to hvad ([`d8c49ba`](https://github.com/lotrekagency/camomilla/commit/d8c49baaa74588ec41dd657971d605cdbafd9b3d))
* Added serializer for nested translations ([`4c7bae3`](https://github.com/lotrekagency/camomilla/commit/4c7bae35145bd7791509b4d15904c3ca9376eb2e))
* Added migration to move data to new table scheme ([`99d87f0`](https://github.com/lotrekagency/camomilla/commit/99d87f080dd4ba6f16fe3f0bd74ac166fb927706))
* Added a custom migration to maintain data from hvad tables ([`6d997bd`](https://github.com/lotrekagency/camomilla/commit/6d997bdffc08f4e01895598004ad61f61f98e3f0))

### Fix
* Set Content model itentifier unique together with page fk ([`b58d309`](https://github.com/lotrekagency/camomilla/commit/b58d309cfbea543586a1d20dd40e8cf3608f284d))
* Fix current user union query for sqlite ([`47b4879`](https://github.com/lotrekagency/camomilla/commit/47b48798e4c6bf7b280e16181083453e53035ac7))
* Fix sqlite OperationalError ([`3cbe374`](https://github.com/lotrekagency/camomilla/commit/3cbe3740b58d88149880da7d870c41dd201e139d))
* Fixed to_db_transform in menu nodes childs ([`9ac1c7c`](https://github.com/lotrekagency/camomilla/commit/9ac1c7cf111d35b986125d438fcc4568f9dec28d))
* **model_api:** Get_queryset in viewset instead of queryset ([`4fd8e4b`](https://github.com/lotrekagency/camomilla/commit/4fd8e4b54eb06e78d4169cba98605cd503a5b480))
* Fix ulrnode match ([`9b6628e`](https://github.com/lotrekagency/camomilla/commit/9b6628e23754e5091ebd895760f731b96537ea72))
* Fix disable i18n ([`a87bb03`](https://github.com/lotrekagency/camomilla/commit/a87bb036c86c3cf65bd2bb8e473cf7097d0d122a))
* Fix some sypos in default html ([`e203f88`](https://github.com/lotrekagency/camomilla/commit/e203f88a5531cfa14fb790166fb7c20afc571925))
* Fix page status check ([`d6363a5`](https://github.com/lotrekagency/camomilla/commit/d6363a54ecd7bb883e7337ffde352e55fe07805c))
* Fix urlnodes permalink generations ([`785b844`](https://github.com/lotrekagency/camomilla/commit/785b8443b2e0bf572d199c6d05fca167e35a98d3))
* Fix dynamic pages ([`878a81e`](https://github.com/lotrekagency/camomilla/commit/878a81e809bf88f22c6cf4b47a4844a361a72cdd))
* Fix annotate default ([`8e155a8`](https://github.com/lotrekagency/camomilla/commit/8e155a8353edd6dd1e2318cd92217dec83225362))
* Fix annotate ([`d199c88`](https://github.com/lotrekagency/camomilla/commit/d199c88437a327a021c6b0138f5ec834618d4aa9))
* Fix setup.cfg ([`621db85`](https://github.com/lotrekagency/camomilla/commit/621db857f20657b2b9a030283aa323b02280d48a))
* Fix media __str__ function ([`18335fe`](https://github.com/lotrekagency/camomilla/commit/18335fef3ac84e77efc649b4e0e493595a6a7428))
* Inherit ModelSerializer in AbstractPageMixin to be sure some method exists ([`3d440a2`](https://github.com/lotrekagency/camomilla/commit/3d440a289b82f1f7c00f9bd364a398193f1f4aaa))
* Fix UniquePermalinkValidator skipping validation on nested bases sublclasses ([`b089d67`](https://github.com/lotrekagency/camomilla/commit/b089d678bc48dad160acd804d449336a695a7df6))
* Skip update child on page creation to prevent missing relation checking ([`7f9f0b2`](https://github.com/lotrekagency/camomilla/commit/7f9f0b2015f38b8f5320587390fa6b3564b2095d))
* **media:** Fix media search scope ([`a729489`](https://github.com/lotrekagency/camomilla/commit/a729489cdc4c4b443fcbd32f8cafdca29be8534e))
* Prevent listing models without an url_node ([`5811b67`](https://github.com/lotrekagency/camomilla/commit/5811b67b89e3c9f0c8901547a29de07593118763))
* Fix model field naming to grant backward compatibility ([`73cd873`](https://github.com/lotrekagency/camomilla/commit/73cd873259712e6665ca572f95a3c00d4b298440))
* Fix translation update in translation serializer ([`1c372f8`](https://github.com/lotrekagency/camomilla/commit/1c372f80483ba0c73ca9ca9325bf075c112917fd))

### Documentation
* Update docs ([`6dcaaf6`](https://github.com/lotrekagency/camomilla/commit/6dcaaf66d1dea2a89bda421c5928536ece96b9e8))
* Update readme ([`92a219d`](https://github.com/lotrekagency/camomilla/commit/92a219d17e5bc5878d2b21c571f1c58ca77aa072))

## v5.8.5 (2023-03-07)
### Fix
* **related:** Nest mixing now is taking depth directly from constructor ([`63c5ae5`](https://github.com/lotrekagency/camomilla/commit/63c5ae5d1c8444bec8b68afac20e2e57fb3b944e))
* **related:** Fix related serializer trying to set queryset on readonly models ([`bd2eb4f`](https://github.com/lotrekagency/camomilla/commit/bd2eb4f9ce2eee5d9807ff656acee6e2c1584170))

## v5.8.4 (2022-12-21)
### Fix
* Fix jsonPatch mixin for trans jsons ([`e0c9236`](https://github.com/lotrekagency/camomilla/commit/e0c9236994fa2a776702c83f14db7496fdcc6450))

## v5.8.3 (2022-12-21)
### Fix
* Fix potential recursion error in NestMixin and take nesting depth from settings ([`647114c`](https://github.com/lotrekagency/camomilla/commit/647114c0b32a556773fe657929a9e3d86254b295))
* Fix recursive nestmixin functions ([`e83586e`](https://github.com/lotrekagency/camomilla/commit/e83586eba127e970b714d78b2cb0ff353731d6fc))

## v5.8.2 (2022-12-21)
### Fix
* Fix nested translations mixins ([`2c17ed8`](https://github.com/lotrekagency/camomilla/commit/2c17ed86d2169df67f2e14b37518e8dc16b6a121))

## v5.8.1 (2022-12-20)
### Fix
* Fix potential recursion error in NestMixin ([`f337155`](https://github.com/lotrekagency/camomilla/commit/f33715549ecb2555eba07ddc2a676e314e48c235))
* **media:** Allow json parser in media for patch requests without files ([`b117229`](https://github.com/lotrekagency/camomilla/commit/b1172297f22cf032c41efefe6a58b206c34d5e2b))
* Show all permissions on profile serializer ([`fb1dc5e`](https://github.com/lotrekagency/camomilla/commit/fb1dc5ee3e27dec4d382e6a06a60599ab82cff1e))
* **media:** Allow json parser in media for patch requests without files ([`00b1d24`](https://github.com/lotrekagency/camomilla/commit/00b1d24a0de19c3a4cfb0bbeafba9e48e06c46ce))
* Show all permissions on profile serializer ([`e2a0116`](https://github.com/lotrekagency/camomilla/commit/e2a011602520945c9835091797d3d7ca508f0f52))

## v5.8.0 (2022-12-20)
### Feature
* **rest_framework:** Go down in nested relation with updatable serializers, DEFAULT_NEST_DEPTH = 10 ([`d22ea66`](https://github.com/lotrekagency/camomilla/commit/d22ea664820e8b5843435aaa7c279502888992f0))
* Optimize many related field to fetch all existing objects ([`8ba3982`](https://github.com/lotrekagency/camomilla/commit/8ba39828c3dbf3c16c5cc89c38e69fb939c8a062))

### Fix
* Fallback media api translations ([`e279f7a`](https://github.com/lotrekagency/camomilla/commit/e279f7ad4eec933ddb4f43b85f0498d1fbf3d17b))
* Fix patch method overriding json field ([`faf7e4b`](https://github.com/lotrekagency/camomilla/commit/faf7e4b5586801639d3633e6db37c0d1e95d9d15))
* Handle ints in many related fields ([`eb7140a`](https://github.com/lotrekagency/camomilla/commit/eb7140a03d0b933939fd6b163744420bc8f9cf59))
* **serializers:** Added BaseModelSerializer to default serializers of RelatedFields ([`e9a37b5`](https://github.com/lotrekagency/camomilla/commit/e9a37b54c0e15acdd7c95ed008b6b5b9722d13c5))
* **page:** Added safe page translation getter in get_page ([`bea64d7`](https://github.com/lotrekagency/camomilla/commit/bea64d7890d9713f1d9043902b9dd9cfe30f7ce9))
* **db:** Added trigram extension in migrations ([`bdadea1`](https://github.com/lotrekagency/camomilla/commit/bdadea19f56bfe1a518f020ec18615e448a3df2d))

## v5.7.7 (2022-08-12)
### Fix
* Fix bad typechecking in BaseModelSerializer ([`5063abf`](https://github.com/lotrekagency/camomilla/commit/5063abfddb47e79cd7ec7b16ce43536021138f55))

## v5.7.6 (2022-08-12)
### Fix
* Fix BaseModelSerializer related field injectig serializer kwargs in wrong class ([`a212c2f`](https://github.com/lotrekagency/camomilla/commit/a212c2fa5fd611fb63899a05026a78ff5f3d4d02))

## v5.7.5 (2022-08-11)
### Fix
* Explicit default_auto_field in app config to prevent unwanted migrations ([`ec33de8`](https://github.com/lotrekagency/camomilla/commit/ec33de87be8f7fc7fc466070e8fe20b7e75ef438))

## v5.7.4 (2022-08-02)
### Fix
* Added missing migrations ([`e57989e`](https://github.com/lotrekagency/camomilla/commit/e57989e7174374bdcff19d042956327e12b65fe4))
* Fix media migration to be compliant with hvad ([`dc5e83a`](https://github.com/lotrekagency/camomilla/commit/dc5e83ad0d639024319a49ac00b01f8845fbe9f1))
* Fix makefile ([`925a270`](https://github.com/lotrekagency/camomilla/commit/925a2706f00c2b6ab5cc9055a557192a4bbd8d4a))
* Added missing migrations for django 4 ([`8a79998`](https://github.com/lotrekagency/camomilla/commit/8a79998e39c9555385ab0d9e87f299b0ede2883d))

## v5.7.3 (2022-05-16)
### Fix
* Fix Arrayfield import ([`2cfdaca`](https://github.com/lotrekagency/camomilla/commit/2cfdacacb63d59cea79ae59f0c3d9839efe56088))
* Fix jsonfield imports ([`be4b566`](https://github.com/lotrekagency/camomilla/commit/be4b56622df269ee5d200dc5666536b39e7fe0cc))

## v5.7.2 (2022-05-13)
### Fix
* Fix get page to work with new hvad ([`2cd8b89`](https://github.com/lotrekagency/camomilla/commit/2cd8b8948df44fd82c214835770e92b10a3f5512))
* Fix camomilla filter content to work with new hvad ([`0193509`](https://github.com/lotrekagency/camomilla/commit/019350929c19cccdfedbdfc2b493039484a08400))
* Update camomilla template to support new django admin static ([`92afbc0`](https://github.com/lotrekagency/camomilla/commit/92afbc07a1345cf19ed4a5a83317f7658b008804))
* Fix gettext_lazy import deprecated in django4 ([`626dfe1`](https://github.com/lotrekagency/camomilla/commit/626dfe16a9fb6457e463ac995eb9d4d809c51e22))

## v5.7.1 (2022-03-30)
### Fix
* Fix circular import error ([`8b3f6ff`](https://github.com/lotrekagency/camomilla/commit/8b3f6ff2d7a01a2f138506ef4ad94fe78b691521))
* Fix session login urls ([`2688c1a`](https://github.com/lotrekagency/camomilla/commit/2688c1aae082654bebd84f3bfd8f2b74104fa930))
* Fix drf session authentication ([`538e709`](https://github.com/lotrekagency/camomilla/commit/538e709dcc8fd2799b4063c265687b2e0315c076))

## v5.7.0 (2022-03-14)
### Feature
* Added ordering to Articles Categories and Pages ([`8cb6d75`](https://github.com/lotrekagency/camomilla/commit/8cb6d752e462462c37add877c056827fddb491cc))
* Added meta to Articles Categories and Pages ([`f859c37`](https://github.com/lotrekagency/camomilla/commit/f859c370add3b34c081edccc4925c0cd99064d42))
* Meta mixin for models 🦹 ([`88c4b4a`](https://github.com/lotrekagency/camomilla/commit/88c4b4afbfc042ea024c9f4ab6090ccb5b73b272))
* Added ordering mixin for rest framework inspired by django adminsortable2 ([`cb619bc`](https://github.com/lotrekagency/camomilla/commit/cb619bcb10650174d8e01835fdb9ecf44ece81a7))

### Fix
* Fix meta mixin methods ([`7d7e3a8`](https://github.com/lotrekagency/camomilla/commit/7d7e3a80bda93a5faec92ebe52ed7be28635790d))
* Fixed reverse ordering in update_order endpoint ([`b8ae096`](https://github.com/lotrekagency/camomilla/commit/b8ae0962bdb75895945b0cc696fb64647e079b31))
* Fix pagination ordering without default order field ([`ca07303`](https://github.com/lotrekagency/camomilla/commit/ca07303c951fe4e6142a8af74ff282d0f90c67c2))

## v5.6.1 (2022-03-01)
### Fix
* Fix pagination mixin to provide order filter and search also for unpaginated queries ([`62e8b01`](https://github.com/lotrekagency/camomilla/commit/62e8b01433aac97a5b70de6197f7bb957e5abf46))

## v5.6.0 (2022-02-26)
### Feature
* Added permission classes to media api ([`558cac2`](https://github.com/lotrekagency/camomilla/commit/558cac2a2b852dcd76d2ad20ce1ab14b4ccb01b0))
* Auto-order pagination mixins ([`125dd71`](https://github.com/lotrekagency/camomilla/commit/125dd71b05faa6554a9def76bd664b837ca8d8fe))
* **serializers:** Automagically 🧙 create nested serializers at runtime avoiding the need of declaring RelatedField classes ([`4748786`](https://github.com/lotrekagency/camomilla/commit/47487860494b56f5fdbff11b4bcc1790e2f9581a))

### Fix
* Fix paginate stack oredering ([`685cf8d`](https://github.com/lotrekagency/camomilla/commit/685cf8dbca2aae00fd2536ed1e1dca6696e88734))

## v5.5.2 (2022-02-14)
### Fix
* Fix djsuperadmin reverse url ([`035d377`](https://github.com/lotrekagency/camomilla/commit/035d377ef9c4dfc25516103542c0aea28a0445a6))

## v5.5.1 (2022-02-14)
### Fix
* Fix RelatedField allow_insert condition ([`90ba04f`](https://github.com/lotrekagency/camomilla/commit/90ba04f2520bf131c95145121362984535f367e2))
* Fix serarchfield for article viewset ([`2c9cda4`](https://github.com/lotrekagency/camomilla/commit/2c9cda4f387bc4bbc5909f7f40ebd484591cb402))
* Added missing migration ([`a018f0f`](https://github.com/lotrekagency/camomilla/commit/a018f0f125e68548492d3fd74a5cd8bddda61293))
* Refactor filefield and fix bad return value ([`1f1a36a`](https://github.com/lotrekagency/camomilla/commit/1f1a36aaa2fad7e43a348ef2513e1aaabdddaae3))
* Fix related field trying to insert new values all the time ([`2465598`](https://github.com/lotrekagency/camomilla/commit/246559814ef351d2cd010fd6f7385777dd075cf2))

## v5.5.0 (2022-02-12)
### Feature
* **api:** Brand new serializators views and permissions for users endpoint ([`0f5b824`](https://github.com/lotrekagency/camomilla/commit/0f5b824c0c614d9ec8fbb1ffd04644e3d30e774c))
* **api:** Added trigram search mixin to medias ([`0002c8b`](https://github.com/lotrekagency/camomilla/commit/0002c8b40a317b3d6bae64c1c12764e31e59cb6c))

### Fix
* Fix File fields imports ([`3a0af76`](https://github.com/lotrekagency/camomilla/commit/3a0af764afefc88336bcb0646e13dc3c9deee609))
* Added creation logics for Related fields ([`56f20a5`](https://github.com/lotrekagency/camomilla/commit/56f20a5df522035ef5bbdca6e8c67bfa40daf274))
* Integrate Camomilla fields in Base model serializers ([`3556d33`](https://github.com/lotrekagency/camomilla/commit/3556d33c7343208b9f7b0e380bb1614c24298169))
* Added FileField and ImageField to fix drf Fields ([`7fc3160`](https://github.com/lotrekagency/camomilla/commit/7fc3160b493cc102ffa1be029e651bc3196266cc))
* Article permalink is now slugfield to prevent bad inputs ([`aafd92c`](https://github.com/lotrekagency/camomilla/commit/aafd92cb518fe5e768ad3fd6f515af0c8599747a))
* Fix article serializer missing categories ([`93b4284`](https://github.com/lotrekagency/camomilla/commit/93b42840980da194dd6b40646d7d5685c7da930a))

## v5.4.2 (2022-01-18)
### Fix
* Fix versioning ([`39b5226`](https://github.com/lotrekagency/camomilla/commit/39b522637ff79c7ff05237d1ad85e1cae26d2a94))
* Added min max range to requirements ([`6841054`](https://github.com/lotrekagency/camomilla/commit/6841054d71c0704919b446eb8ed542d3fb08a873))

## v5.4.1 (2022-01-17)
### Fix
* Loosen the range of requirements package versions ([`96d491b`](https://github.com/lotrekagency/camomilla/commit/96d491b4ff0aba269624eb7a27b1f3cd55946721))

## v5.4.0 (2022-01-13)
### Feature
* **media:** Added mime_type column to media model ([`4771068`](https://github.com/lotrekagency/camomilla/commit/4771068d2e54779a3d6e38ee9b447fb04c73539c))
* **api:** Added search to medias ([`905661d`](https://github.com/lotrekagency/camomilla/commit/905661d874b5ff2e22ea8b508c46d1ccfc70c0e7))
* **media:** Added option to override Media file on update from api to maintain same url ([`8d6371f`](https://github.com/lotrekagency/camomilla/commit/8d6371ff94e460f2e84efde45882d7d192b7cce6))

### Fix
* **media:** Added opetation to db  migration to recalc old media with the new mime_type feature ([`a7afd2d`](https://github.com/lotrekagency/camomilla/commit/a7afd2d53ba2b2f27d0d06fb6dba131368fdcc6e))
* **media:** Mime filter parsing works also in folder viewset ([`4149e92`](https://github.com/lotrekagency/camomilla/commit/4149e92e6c67e5f96219f02859a3aaa3f748553d))

## v5.3.0 (2021-12-17)
### Feature
* **api:** Handle multisort on PaginateStackMixin ([`40080f4`](https://github.com/lotrekagency/camomilla/commit/40080f4542c8e0dd4c8b36bb5cf5de6e078c3314))

## v5.2.0 (2021-12-17)


## v5.1.0 (2021-12-17)
### Feature
* Added image properties into media model ([`09cb481`](https://github.com/lotrekagency/camomilla/commit/09cb4818b2e3207eab7a12361f5e273b17edd1d0))
* Option to remove pagination on views ([`3e6fc48`](https://github.com/lotrekagency/camomilla/commit/3e6fc489db8b01f488ffebedd93f614c01d9e8d3))

### Fix
* Fix sqlite compatibility problems ([`4cde4fc`](https://github.com/lotrekagency/camomilla/commit/4cde4fc6c5f0e0b0d76e2020943de6d0bc973a49))
* Fix app name ([`13bb12d`](https://github.com/lotrekagency/camomilla/commit/13bb12d75bc9072a9ff150a7b408157f022c9299))
* Added search field to article viewset ([`1bd4b5f`](https://github.com/lotrekagency/camomilla/commit/1bd4b5f0681885b19bb2043d7622c8b3e77b9689))
* Fix articles and pages serializers requiring RelatedField fields. ([`c4fd330`](https://github.com/lotrekagency/camomilla/commit/c4fd330fb06dc3d49de4100865376a9eedb3f6f6))

## v5.0.3 (2021-10-26)


## v5.0.2 (2021-10-26)

