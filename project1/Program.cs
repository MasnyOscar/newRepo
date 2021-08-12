using System;

namespace project1
{
    class Program
    {
        static void Main(string[] args)
        {
            greetUser();

            var userLogin = getLogin();
            var userPassword = getPassword();
            var correctLogin = "oskar";
            var correctPassword = "admin";

            bool userAnswer = false;

            while (!userAnswer)
            {
                Console.Clear();

                if (userLogin == correctLogin && userPassword == correctPassword)
                {
                    Console.Clear();
                    var message = "Correct data";
                    messageColor(ConsoleColor.DarkGreen, message);
                    break;
                }
                userLogin = getLogin();
                userPassword = getPassword();
            }
        }

        static void greetUser()
        {
            Console.WriteLine("Welcome in our page!"); 
        }

        static void messageColor(ConsoleColor color, string message)
            {
            Console.ForegroundColor = color;
            Console.WriteLine(message);
            Console.ResetColor();
            }

        static string getLogin()
        {
            var message = "Enter login:";
            messageColor(ConsoleColor.Blue, message);
            var login = Console.ReadLine();

            login = login.ToLower();
            return login;
        }


        static string getPassword()
        {
            var message = "Enter password:";

            messageColor(ConsoleColor.Blue, message);

            var password = Console.ReadLine();
            return password;
        }

    }
}