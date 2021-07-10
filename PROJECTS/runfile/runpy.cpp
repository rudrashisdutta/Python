#include <iostream>
#include <string>
#include <Windows.h>
#include <fstream>
using namespace std;
int filenamecheck(string &filename);
void Colour(int c);
void OpenPathFile(string file);
int main()
{
PYTHONCONSOLE0:
    system("cls");
    Colour(7);
    cout << "PYTHON CONSOLE 1.0\n\n";
PYTHONCONSOLE1:
    string command = "", keyword = "", filename = "";
    cout << "$$>> ";
    Colour(9);
    getline(cin, keyword, ' ');
    Colour(7);
    getline(cin, filename);
    if (keyword == "py" || keyword == "python" || keyword == "runpy")
    {
        if (filenamecheck(filename) != 3 || filenamecheck(filename) != 0)
        {
            command = "python.exe " + filename;
            system(command.c_str());
        }
        else
            cout << "Not a valid filename.\n";
        goto PYTHONCONSOLE1;
    }
    else if (keyword == "crt" || keyword == "create")
    {
        if (filenamecheck(filename) != 3 || filenamecheck(filename) != 0)
        {
            OpenPathFile(filename);
        }
        else
            cout << "Not a valid filename.\n";
        goto PYTHONCONSOLE1;
    }
    else if (keyword == "del" || keyword == "dlt" || keyword == "delete")
    {
        if (filenamecheck(filename) != 3 || filenamecheck(filename) != 0)
            int b = remove(filename.c_str());
        else
            cout << "Not a valid filename.\n";
        goto PYTHONCONSOLE1;
    }
    else if (keyword == "cls" || keyword == "clear" || keyword == "clean")
        goto PYTHONCONSOLE0;
    else
    {
        cout << keyword << " : The term ' " << keyword << "' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path was included, verify that the path is correct and try again.";
    }
}
int filenamecheck(string &filename)
{
    int i = 0, flag = 0;
    if (filename == ".py")
        flag = 3;
    else
    {
        int len = filename.length();
        if (filename[len - 3] == '.' && filename[len - 2] == 'p' && filename[len - 1] == 'y')
            flag = 1;
        else
        {
            filename = filename + ".py";
            flag = 1;
        }
    }
    return flag;
}
void Colour(int c)
{
    SetConsoleTextAttribute(GetStdHandle(STD_OUTPUT_HANDLE), c);
}
void OpenPathFile(string file)
{
    ofstream open(file.c_str(), ios::app);
    open.close();
}