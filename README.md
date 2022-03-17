<div align="center">

# Manfred Awesomic CV

The MAC (or Manfred Awesomic CV) is a(nother) naive attemp to create **a standard open source format to define and share CVs**. The format is defined as a JSON Schema to validate CVs stored as JSON files.

[Why use it](#why-use-it) •
[How to use it](#how-to-use-it) •
[Who use it](#why-use-it) •
[Who are you?](#who-are-you) •
[Roadmap](#roadmap)  
<br />
<br />
<br />
!["JSON Schema"](https://github.com/getmanfred/mac/blob/master/assets/readme/schema_screen_capture.png?raw=true "JSON Schema")
<br />
 <br />
!["MAC Sample"](https://github.com/getmanfred/mac/blob/master/assets/readme/MAC_sample.gif?raw=true "MAC Sample")
  
</div>  

## Why use it

There are A LOT of CV formats, and some of them are a nice try to define a universal CV format, but we think that **a CV should include not only what candidates are or know but also what they are interested in and what they want to become**.

Like most open-source projects, the first use case was found in the company where the first contributors worked. Manfred is committed to the idea that **every person should keep control over their personal and professional data**. This means that they should be able to export their data from any platform in a machine-readable format with **a Model Definition to process that data efficiently**. This is how the MAC was born.


!["MAC Design"](https://github.com/getmanfred/mac/blob/master/assets/readme/MAC_first_design.png?raw=true "MAC Design")


## How to use it

You just need to copy, download or reference [the schema](https://github.com/getmanfred/mac/blob/master/schema/schema.json) to validate a new CV, built as a JSON file from scratch, or a JSON generated previously (for example, [this sample](https://github.com/getmanfred/mac/blob/master/samples/deafult_sample.json)).

To get started, you can copy both schema and sample in an **online validator** like [jsonschemavalidator.net](https://www.jsonschemavalidator.net/) or [liquid-technologies.com/online-json-schema-validator](https://www.liquid-technologies.com/online-json-schema-validator).

!["JSON Schema"](https://github.com/getmanfred/mac/blob/master/assets/readme/MAC_online_validator_example.png?raw=true "JSON Schema")

You also have implementations to validate a JSON file programmatically in almost every coding language:

* [AVJ (JavaScript)](https://ajv.js.org/)
* [Snow (Java)](https://github.com/ssilverman/snowy-json)
* [jschon (Python)](https://jschon.readthedocs.io/en/latest/)
* ... and [much more](https://json-schema.org/implementations.html)

> :warning: **The current MAC Schema has been designed using the 2019-09 Specification Draft**: When choosing a validator, please, check if it's compliant with the 2019-09 Draft. You can get much more information about the JSON Schema Specification in [json-schema.org](https://json-schema.org/).

The Schema is documented by itself, but it's much easier to get "the big picture" with a graphical representation:
<br />
<br />
!["MAC Diagram"](https://github.com/getmanfred/mac/blob/master/assets/readme/MAC_diagram.png?raw=true "MAC Diagram")
<br />

## Who use it

A bunch of Tech Startups, IT Consulting Companies and Recruiting Platforms already use the MAC as an interchangeable format **to unlock the data of their users, candidates and employees and give them back the power to use it wherever they want**.

<a href="https://www.getmanfred.com/" target="_blank"><img alt="Manfred" src="https://pbs.twimg.com/profile_images/946845160004112384/ap8_xjIa_400x400.jpg" width="170"/></a> <a href="https://www.sngular.com/" target="_blank"><img alt="SNGULAR" src="https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/ympwkuxhx9lusfwrfbbb" width="170"/></a>

## Who are you?

TBD

## Roadmap

TBD
