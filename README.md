# PytherCIS
Simple python bindings/client library for the Ethercis openEHR CDR (and other compatible openEHR Clinical Data Repositories)


## Installation

`git clone` this repository
```
git clone git@github.com:Epidurio/pythercis.git
```
Install an EtherCIS clinical data repository to interact with. The easiest way to get access to one of these is:
* use the resources of the [Code4Health Platform](https://platform.code4health.org/#/), which gives you free dev/testing access to an instance of the non-free, proprietary, Marand openEHR CDR. Both EtherCIS and Marand aim to adhere to the same openEHR standards and a similar REST API design, so they are cross-compatible although no guarantee of call-for-call API-level compatibility is given.
* install an instance of the [EtherCIS](http://ethercis.org/) open source openEHR CDR locally, by following the instructions below. (note the prerequisites: [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/))

Clone the `docker-ethercis` repository
```
git clone https://github.com/operonflow/docker-ethercis.git
```

Enter the relevant directory
```
cd docker-ethercis
```

Start up Docker Compose, which will create Docker containers for the EtherCIS server and its PostgresQL database.
```
docker-compose up
```

After the startup procedure, you should see a message from the EtherCIS server to say it is 'listening' on some random URL like 'host:67e9af32b8a4 port:8080', which is an internal Docker reference. You should be able to access the server on `localhost:8080`.

Now set up your PytherCIS client:

`cd ..` to get back up into the parent directory

`cd pythercis` to enter the cloned PytherCIS directory

Now follow the rest of the Getting Started tutorial below


## Getting Started: usage from the Python shell
As an example, I am describing usage in the interactive Python shell. Depending on your platform, there can be different ways to access the Python Shell. Consult the [Python docs](https://www.python.org/downloads/) for more help

```
╰─$ python
Python 3.5.2
Type "help", "copyright", "credits" or "license" for more information.
>>> import pythercis
```

Instantiate an Ethercis object and set the base URL of the Ethercis server
```
>>> ehr = pythercis.Pythercis('http://localhost:8080')
```

Authenticate to the EtherCIS server with a username and password (a list of valid passwords for a vanilla EtherCIS install are [here](https://github.com/ethercis/ethercis/blob/master/examples/config/security/authenticate.ini)). The following combination (root/secret)should work.
```
>>> session = ehr.create_session('root', 'secret')
{
  "meta" : {
    "href" : "rest/v1/session?sessionId=sessionId:172.18.0.3-root-1519837236100-794709294-19"
  },
  "action" : "CREATE",
  "sessionId" : "sessionId:172.18.0.3-root-1519837236100-794709294-19"
}

```

You should get back a JSON response in the python shell, containing a `sessionId`, which tells you that you are authenticated to the server. This `sessionId` is needed for all your future interactions with the EtherCIS server. PytherCIS will cache this sessionId for you and pass it into the HTTP headers of all future interactions automatically. You can also access it via the method `Pythercis.session_id`.


## Setting up openEHR Templates
openEHR CDRs don't come with any templates out of the box, so in order to do anything useful with the CDR, you'll need to upload a template or set of temlpates. This step is akin to running a schema against a conventional database, or running a migration in a web framework's ORM. Templates are uploaded via the REST API.

There are some example openEHR templates in the `operational_templates/` subdirectory of this repository. The technical template artefact that is uploaded is called an Operational Template, and these can also be created by exporting an operational template from the [openEHR Template Designer](https://www.openehr.org/downloads/modellingtools) UI.

List available templates on the EtherCIS server
```
>>> ehr.list_templates()
{
  "meta": {
      "href": "rest/v1/template"
  },
  "templates": []
}
```
We were of course expecting that there wouldn't be any templates there initially, but this step serves as a nice way to check everything is working fine and we'll repeat it again after we've uploaded our template, and we should see the template listed.

Upload an openEHR template to the EtherCIS CDR with the relative path
```
>>> ehr.upload_template('/path/to/operational/template/')
{
    "meta": {
        "href": "rest/v1/template"
    },
    "action": "CREATE",
    "templateId": "HDAY - Epidural Report.v0"
}
```

List available templates on the EtherCIS server again
```
{
  "meta" : {
    "href" : "rest/v1/template"
  },
  "templates" : [ {
    "path" : "/etc/opt/ecis/knowledge/operational_templates/HDAY - Epidural Report.v0.opt",
    "lastAccessTime" : "2018-02-28T12:18:29.911170Z[Etc/UTC]",
    "lastModifiedTime" : "2018-02-28T12:18:29.911170Z[Etc/UTC]",
    "templateId" : "HDAY - Epidural Report.v0",
    "createdOn" : "2018-02-28T12:18:29.911170Z[Etc/UTC]"
  } ]
}
```
