#DIY Transparency Report
DIY Transparency Report is an application that makes it simpler to define and create transparency reports for your organization.

DIY Transparency Report is a Python application that runs a webserver that serves a web interface. Point your web browser to http://localhost:5000 to use the app.

See Appendix II of [A Guide to Transparency Reporting for Canadian Businesses Using the DIY Transparency Report Tool for usage instructions](https://www.telecomtransparency.org/wp-content/uploads/2016/06/Transparency-Reporting-Tool-Documentation-1.0.pdf).

## Installing and opening the app
We provide some useful scripts for Windows and Mac users to make it easier to install and launch the application.

### Windows
Make sure you have Python 2.7.x installed on your machine (The below scripts assume Python is installed to C:\Python27). https://www.python.org/downloads

Next, if you don't have pip installed, install it following the official guide: https://pip.pypa.io/en/stable/installing/

Next, double click `windows-install.bat` to install the required software libraries.

Finally, double click `windows-diy-transparency-run.bat` to run the app. Make sure you keep the command prompt window open while you use the app.

### Mac
Double click on `Install.app` to install the app. This will install the required software libraries if they don't exist. 

Next, to run the app, double click on `DIY Transparency.app` to run the application server and open your web browser. Make sure you keep the terminal window open while you use the app.

**NOTE: You'll need to give `Install.app` and `.DIY Transparency.app` permission to run on your computer. If you don't want to do that, follow the Linux instructions below.**

### Linux
Make sure you have Python 2.7.x, pip, and virtualenv (apt-get install virtualenv) installed.

In the terminal, in the project folder, run

	bash install.sh

Once installation is, to launch the app server you can run:

	bash diy-transparency-run.sh

