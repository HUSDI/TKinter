Info:
Most of this code was created by me, HUSDI.
I don't take credit for the frame layering
since I didn't come up with it.

==============================================================
How to add "windows" (like the Login Window):
==============================================================
1. Create a class that inherits form tk.Frame
2. Def an __init__ method like this:

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
	
	# Add your code

3. Go to the for loop in the class "EMailPrg"
   and add your new class name to it.
   Example:

    for F in (LoginPage, RegisterPage, PageOne, NewClassName)


==============================================================

!IMPORTANT!
Use this progam on your own risk!
Don't enter your real usernames and passwords since everyone
can just read them from the json file!

I assume no damage or loss to property, privacy or data that may result from
alteration or use of this and all my other programs and scripts.