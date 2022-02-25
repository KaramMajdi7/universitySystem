# University System

This project was created using Python, and using the Tkinter library, and including a database with MySQL, 
and by including the OOP concepts and the Software Engineering concepts, and the most important thing about this particular project is 
the Software Engineering concepts I used and devloped and the workflow i followed from analysis, design, implementation and testing, and here is some 
of the design models I used:

First of all the use case diagram for the project which describes the stakeholders of the sytem and each action for each user, and the common 
actions between them:
![image](https://user-images.githubusercontent.com/74671857/155380605-e42c5090-c47d-444b-9560-73dc59873920.png)

and then the Log in activity diagram, which describes the workflow of the log in action for each actor and what happens in a scucessful log in, and 
what choices the actor can pick:

![image](https://user-images.githubusercontent.com/74671857/155380761-4e3d2aa5-fa60-4a58-969a-d2ee4743fcdb.png)
![image](https://user-images.githubusercontent.com/74671857/155380835-8d53082f-7787-4f3d-adae-866981eb059f.png)


and then the first choice which is the Gpa Calculator, which is the biggest one in context of functionality in this project, and it's based on my university material,
and the GPA system for the university, and that you can send the calculated GPA usnig your number or save the details to your device, and the activity diagram is as 
follow:

![image](https://user-images.githubusercontent.com/74671857/155380966-35425e9c-a448-447e-a7c3-99e633bd8f3d.png)
![image](https://user-images.githubusercontent.com/74671857/155381038-38347653-7167-4e8d-a1f5-f60cbee0c230.png)


and the second choice is the Material Details, which is a simple in the interface side, and it contains the material of the computer science faculty in my university,
and the plans you could follow if you want to finish in 3 and half years or in 4 years, and then the search bar, where you could enter any material code for CS, and
it will return a window with the details about that material and when to take and how to study it and a link for some exams you could solve, and here is the activity 
diagram:

![image](https://user-images.githubusercontent.com/74671857/155381171-9acd14df-c4e1-4bd6-8461-ce52aef9ca76.png)
![image](https://user-images.githubusercontent.com/74671857/155381242-195f5be2-4d6f-4e59-8836-385106f3c101.png)


And now let's take a look at the implementation using Python and the Tkinter library and some other libraries, and having a databse to store all the log in and registration information in a table.

First of all lets take a look at the Register window:

![register1](https://user-images.githubusercontent.com/74671857/155679889-e1725e6e-13ae-4472-a79f-744aca08c913.JPG)

So here we have at the right the form to register in the system and when you finish filling this form it will save all the information in the database MySQL that we have, and after that:

![register2](https://user-images.githubusercontent.com/74671857/155680092-98f247e4-b4c8-4c2a-be3c-59f160b7560f.JPG)

You will have an email and password so now you could click at the button at the left which is log in.

And now, here is the Log In Window:

![logIn1](https://user-images.githubusercontent.com/74671857/155678934-cfbf74e9-7c1c-47c8-8e0f-0013fae6a56d.JPG)

Here we have an email entry field and a password field that are written by the user and then checked by the database using the pymysql library, and the forget password button here is clicked when you provide a valid email address only, and it looks like this:

![logIn2](https://user-images.githubusercontent.com/74671857/155679234-34c61eab-5add-416b-b0d0-9d63dd28035f.JPG)

Here it's asking for the question that you provided when you first registered and the answer for it, and the pymysql check for it, and then changes your passwrod if it was valid, and at last when you log in successfully it will give you 2 options:

![logIn3](https://user-images.githubusercontent.com/74671857/155679581-12b6795b-5565-42ce-ae67-3a0e5b6e70c4.JPG)

Where each one of these options will take you to a new window so lets first take a look at the GPA Calculator button:

![gpaCalc1](https://user-images.githubusercontent.com/74671857/155680253-8fb89974-a97d-48f3-9abb-e69ccb3d0148.JPG)

Here we have the material of CS field in my university, so first you will pick the material you want to calculate and the grade you got, then provide your name, your ID, the number of hours you finished and your password, then when you click the GPA button it will provide the calculated GPA at the bottom left, and the view button will give you the detail of your semester, so lets take a look at this:

![gpaCalc2](https://user-images.githubusercontent.com/74671857/155680853-1693c72c-db43-45ce-8bb4-b0360b419a45.JPG)

and the view button will give this detaila and also the hours left for you:

![gpaCalc3](https://user-images.githubusercontent.com/74671857/155683555-254cfef8-659e-48ec-808a-3f608efd8091.JPG)

And at last the save button will Save the details of your calculated GPA as a text file, and then the Send buttton will send these details to anyone you want by putting their number in the mobile number field by using the pywhatkit library, so let's take a look at it:

![gpaCalc4](https://user-images.githubusercontent.com/74671857/155684066-4c207ee5-e827-4483-aa2c-9b0b28a1441f.JPG)

And then we have the second option after the successful log in which is the Material Info window, and here it is:

![materialInfo1](https://user-images.githubusercontent.com/74671857/155684267-45e35360-68fd-40a5-89f9-7a7ecc6c2294.JPG)









