##introduction to Cyber Lab##

Django based vulnerable webservice. This is a web service intended to be hosted locally in a university cyber lab. The intention of the cyber lab is two fold; one, this tool is to host a series of learning materials and activities for students to complete. Two, this web service is deliberately vulnerable so that it may gather "real" data from student usage and exploitation of this asset can be an end of module activity for students

If the final task is to the exploitation of this service, it is recommended that tutors hide unique information or markers in their instance and verify student achievement by confirming these markers with the students. More advanced students may be tasked with implementing mitigations to this web service, but each student may need their own instance for this. 

Students should be frequently reminded of the vulnerbility of this web service and thus should not use any real data other than name and student email address. 

The web service is intended to be spun up and replaced quickly and easily, as (hopefully) the vulnerabilities should mean that it gets broken or altered regularly. Tutors should note this, and if using the sevice for assessments to ensure that results are recorded away from the web service. Students should not assume that their work or account will be there when they return, and should behave accordingly.

##content##

Home page: home page and general content pages for cyber lab
Lessons: security testing materials (html format)
Tasks: lab activities to be completed away from cyber lab (virtual box, etc)

##TO DO##

To do:
-sign up/log in
-Add lessons
-Add tasks
-Add vulnerabilities
-Export of student records/achievements/account data
-deploy in docker

##vulnerabilities##

1. Weak admin credentials
2. Weak credential storage