# qp_generator
Question paper review and generation system

A question paper review generation system mainly aims to generate the question
paper based on various course outcomes and blooms taxonomy levels. In this Project
their will be 3 login system one for the faculty who prepare’s the question paper and
other for the reviewer the one who reviews the paper and another one for admin.
In the faculty needs to login and enter the questions and then this question’s will
be saved in the database, than the reviewer needs to login and review the questions
entered by the faculty and than if their is any error in the questions entered than
the reviewer needs to send a feedback message for the faculty to change the question
after the final submission the question paper generated will be displayed in the admins
login page and here the question paper generated is based on the blooms taxonomy
that is (L1, L2, L3, L4, etc) and to assign the blooms taxonomy we have used NLP
tokenization for keywords matching and than the level for the questions is assigned
based on the various outcomes, than the admin can print the question paper or send
the paper for the exam section
