(window.webpackJsonp=window.webpackJsonp||[]).push([[20],{297:function(t,s,a){"use strict";a.r(s);var e=a(14),n=Object(e.a)({},(function(){var t=this,s=t._self._c;return s("ContentSlotsDistributor",{attrs:{"slot-key":t.$parent.slotKey}},[s("h1",{attrs:{id:"🧬-use-structured-json-field"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#🧬-use-structured-json-field"}},[t._v("#")]),t._v(" 🧬 Use Structured JSON Field")]),t._v(" "),s("p",[t._v("The StructuredJSONField is a special type of field that allows you to create a structured JSONField.\nThis kind of field allows you to declare a data structure that will be enforced to the json structure.")]),t._v(" "),s("p",[t._v("To declare a data structure you need to create a class that inherits from "),s("code",[t._v("camomilla.structured.BaseModel")]),t._v(" and declare the fields that you want to use. The Base model is a pydantic model, so you can use all the pydantic features. If you never used pydantic before, you can find the documentation "),s("a",{attrs:{href:"https://pydantic-docs.helpmanual.io/",target:"_blank",rel:"noopener noreferrer"}},[t._v("here"),s("OutboundLink")],1),t._v(".")]),t._v(" "),s("p",[t._v("Let's see an example:")]),t._v(" "),s("div",{staticClass:"language-python extra-class"},[s("pre",{pre:!0,attrs:{class:"language-python"}},[s("code",[s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" camomilla"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("structured "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" BaseModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" StructuredJSONField\n\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("class")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token class-name"}},[t._v("MyStructuredJSONField")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("BaseModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v("\n    name"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v("\n    age"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("int")]),t._v("\n\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("class")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token class-name"}},[t._v("MyModel")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("models"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("Model"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v("    \n    structured_field "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" StructuredJSONField"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("schema"),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v("MyStructuredJSONField"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])])]),s("p",[t._v("In this example we created a model with a StructuredJSONField that will accept only jsons with the following structure:")]),t._v(" "),s("div",{staticClass:"language-json extra-class"},[s("pre",{pre:!0,attrs:{class:"language-json"}},[s("code",[s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    "),s("span",{pre:!0,attrs:{class:"token property"}},[t._v('"name"')]),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"string"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v("\n    "),s("span",{pre:!0,attrs:{class:"token property"}},[t._v('"age"')]),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("0")]),t._v("\n"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n")])])]),s("p",[t._v("If you try to save a json with a different structure, the field will raise a "),s("code",[t._v("ValidationError")]),t._v(".")]),t._v(" "),s("h3",{attrs:{id:"default-value"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#default-value"}},[t._v("#")]),t._v(" Default value")]),t._v(" "),s("p",[t._v("Since the StructuredJSONField is a JSONField, you can use all the JSONField features, like the "),s("code",[t._v("default")]),t._v(" parameter:")]),t._v(" "),s("div",{staticClass:"language-python extra-class"},[s("pre",{pre:!0,attrs:{class:"language-python"}},[s("code",[s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" camomilla"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("structured "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" BaseModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" StructuredJSONField\n\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("class")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token class-name"}},[t._v("MyStructuredJSONField")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("BaseModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v("\n    name"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v("\n    age"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("int")]),t._v("\n\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("class")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token class-name"}},[t._v("MyModel")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("models"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("Model"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v("\n    structured_field "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" StructuredJSONField"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("schema"),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v("MyStructuredJSONField"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" default"),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"name"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"John"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"age"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("30")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])])]),s("p",[t._v("In this example we set a default value for the field. If you try to save a json without the "),s("code",[t._v("name")]),t._v(" or "),s("code",[t._v("age")]),t._v(" fields, the field will be populated with the default value.")]),t._v(" "),s("p",[t._v("You can also use a generator as default value:")]),t._v(" "),s("div",{staticClass:"language-python extra-class"},[s("pre",{pre:!0,attrs:{class:"language-python"}},[s("code",[s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" camomilla"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("structured "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" BaseModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" StructuredJSONField\n\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("class")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token class-name"}},[t._v("MyStructuredJSONField")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("BaseModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v("\n    name"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v("\n    age"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("int")]),t._v("\n\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("def")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token function"}},[t._v("default_value")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v("\n    "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("return")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"name"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"John"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"age"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token number"}},[t._v("30")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("class")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token class-name"}},[t._v("MyModel")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("models"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("Model"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v("    \n    structured_field "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" StructuredJSONField"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("schema"),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v("MyStructuredJSONField"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" default"),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v("default_value"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])])]),s("p",[t._v("In this example we used a function as default value. The function will be called every time a new instance of the model is created.")]),t._v(" "),s("h2",{attrs:{id:"nesting-models"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#nesting-models"}},[t._v("#")]),t._v(" Nesting Models")]),t._v(" "),s("p",[t._v("Structured models can be nested. Let's see an example:")]),t._v(" "),s("div",{staticClass:"language-python extra-class"},[s("pre",{pre:!0,attrs:{class:"language-python"}},[s("code",[s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" camomilla"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("structured "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" BaseModel\n\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("class")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token class-name"}},[t._v("MyNestedModel")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("BaseModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v("\n    name"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v("\n    age"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("int")]),t._v("\n\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("class")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token class-name"}},[t._v("MyOtherNestedModel")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("BaseModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v("\n    name"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v("\n    age"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("int")]),t._v("\n    children"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" MyNestedModel\n    childrens"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("list")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),t._v("MyNestedModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n")])])]),s("p",[t._v("If you need to nest recursively a model, for example a model that as itself as children, you can declare the type as a string:")]),t._v(" "),s("div",{staticClass:"language-python extra-class"},[s("pre",{pre:!0,attrs:{class:"language-python"}},[s("code",[s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" camomilla"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("structured "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" BaseModel\n\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("class")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token class-name"}},[t._v("MyNestedModel")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("BaseModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v("\n    name"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v("\n    age"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("int")]),t._v("\n    children"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v("'MyNestedModel'")]),t._v("\n    childrens"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("list")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),s("span",{pre:!0,attrs:{class:"token string"}},[t._v("'MyNestedModel'")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n")])])]),s("h2",{attrs:{id:"list-of-structuredjsonfield"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#list-of-structuredjsonfield"}},[t._v("#")]),t._v(" List of StructuredJSONField")]),t._v(" "),s("p",[t._v("If you use a list as a default value, the field will adapt the schema to accept a list of the specified type:")]),t._v(" "),s("div",{staticClass:"language-python extra-class"},[s("pre",{pre:!0,attrs:{class:"language-python"}},[s("code",[s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" camomilla"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("structured "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" BaseModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" StructuredJSONField\n\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("class")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token class-name"}},[t._v("MyStructuredJSONField")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("BaseModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v("\n    name"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v("\n    age"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("int")]),t._v("\n\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("class")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token class-name"}},[t._v("MyModel")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("models"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("Model"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v("\n    structured_field "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" StructuredJSONField"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("schema"),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v("MyStructuredJSONField"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" default"),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("list")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),t._v("\n")])])]),s("h2",{attrs:{id:"foreign-key-field"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#foreign-key-field"}},[t._v("#")]),t._v(" Foreign Key Field")]),t._v(" "),s("p",[t._v("There are some special features that you can use with the StructuredJSONField.")]),t._v(" "),s("p",[t._v("If you declare a field with a django model as type, the field will be populated with the instance of the model, as it was a foreign key:")]),t._v(" "),s("div",{staticClass:"language-python extra-class"},[s("pre",{pre:!0,attrs:{class:"language-python"}},[s("code",[s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" camomilla"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("structured "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" BaseModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" StructuredJSONField\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" django"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("contrib"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("auth"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("models "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" User\n\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("class")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token class-name"}},[t._v("MyStructuredJSONField")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("BaseModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v("\n    name"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v("\n    age"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("int")]),t._v("\n    user"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" User\n\n")])])]),s("p",[t._v("At database level the json will store only the model primary key, but when you access the field you will get the instance of the model.\nHence we have a fully working relation inside a json field.")]),t._v(" "),s("h2",{attrs:{id:"queryset-field"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#queryset-field"}},[t._v("#")]),t._v(" QuerySet Field")]),t._v(" "),s("p",[t._v("You can also use an other special type of field: "),s("code",[t._v("camomilla.structured.QuerySet")]),t._v(". This field will store a queryset inside the json field. This is useful when you need to store a list of models. For example:")]),t._v(" "),s("div",{staticClass:"language-python extra-class"},[s("pre",{pre:!0,attrs:{class:"language-python"}},[s("code",[s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" camomilla"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("structured "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" BaseModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" StructuredJSONField"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(",")]),t._v(" QuerySet\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("from")]),t._v(" django"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("contrib"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("auth"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(".")]),t._v("models "),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("import")]),t._v(" User\n\n"),s("span",{pre:!0,attrs:{class:"token keyword"}},[t._v("class")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token class-name"}},[t._v("MyStructuredJSONField")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("(")]),t._v("BaseModel"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(")")]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v("\n    name"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("str")]),t._v("\n    age"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token builtin"}},[t._v("int")]),t._v("\n    users"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" QuerySet"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("[")]),t._v("User"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("]")]),t._v("\n\n")])])]),s("p",[t._v("In this example we declared a field that will store a list of users. The field will be populated with a queryset, so you can use all the django queryset features.\nIn the json structure the field will store only the primary keys of the models, ordered by the queryset order or insertion order.\nWhen you access the django queryset, the order will be preserved. This means that you can manage queryset ordering just saving the json with data in correct order.")]),t._v(" "),s("h2",{attrs:{id:"built-in-cache-system"}},[s("a",{staticClass:"header-anchor",attrs:{href:"#built-in-cache-system"}},[t._v("#")]),t._v(" Built-in cache system")]),t._v(" "),s("p",[t._v("Both Foreign Key and QuerySet fields can lead to performance issues. If you have a lot of instances of django models spread all over the json, the field will make several queries to the database to retrieve the related models.")]),t._v(" "),s("p",[t._v("The structured field has a built-in cache system to avoid this problem 🎉.")]),t._v(" "),s("p",[t._v("The cache system will analyze the json and will make only the stricly necessary queries to the database. The cache system is enabled by default, but you can disable it from camomilla settings:")]),t._v(" "),s("div",{staticClass:"language-python extra-class"},[s("pre",{pre:!0,attrs:{class:"language-python"}},[s("code",[s("span",{pre:!0,attrs:{class:"token comment"}},[t._v("# settings.py")]),t._v("\n\nCAMOMILLA "),s("span",{pre:!0,attrs:{class:"token operator"}},[t._v("=")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n    "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"STRUCTURED_FIELD"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("{")]),t._v("\n        "),s("span",{pre:!0,attrs:{class:"token string"}},[t._v('"CACHE_ENABLED"')]),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v(":")]),t._v(" "),s("span",{pre:!0,attrs:{class:"token boolean"}},[t._v("False")]),t._v("\n    "),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n"),s("span",{pre:!0,attrs:{class:"token punctuation"}},[t._v("}")]),t._v("\n")])])])])}),[],!1,null,null,null);s.default=n.exports}}]);