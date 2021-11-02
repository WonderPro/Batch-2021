Many of the C projects that exist today were started decades ago.

The UNIX operating system’s development started in 1969, and its code was rewritten in C in 1972. The C language was actually created to move the UNIX kernel code from assembly to a higher level language, which would do the same tasks with fewer lines of code.

Oracle database development started in 1977, and its code was rewritten from assembly to C in 1983. It became one of the most popular databases in the world.

In 1985 Windows 1.0 was released. Although Windows source code is not publicly available, it’s been stated that its kernel is mostly written in C, with some parts in assembly. Linux kernel development started in 1991, and it is also written in C. The next year, it was released under the GNU license and was used as part of the GNU Operating System. The GNU operating system itself was started using C and Lisp programming languages, so many of its components are written in C.

But C programming isn’t limited to projects that started decades ago, when there weren’t as many programming languages as today. Many C projects are still started today; there are some good reasons for that.

How is the World Powered by C?
Despite the prevalence of higher-level languages, C continues to empower the world. The following are some of the systems that are used by millions and are programmed in the C language.

Microsoft Windows
Microsoft’s Windows kernel is developed mostly in C, with some parts in assembly language. For decades, the world’s most used operating system, with about 90 percent of the market share, has been powered by a kernel written in C.

Linux
Linux is also written mostly in C, with some parts in assembly. About 97 percent of the world’s 500 most powerful supercomputers run the Linux kernel. It is also used in many personal computers.

Mac
Mac computers are also powered by C, since the OS X kernel is written mostly in C. Every program and driver in a Mac, as in Windows and Linux computers, is running on a C-powered kernel.

Mobile
iOS, Android and Windows Phone kernels are also written in C. They are just mobile adaptations of existing Mac OS, Linux and Windows kernels. So smartphones you use every day are running on a C kernel.

Operating System Kernels Written in C
Databases
The world’s most popular databases, including Oracle Database, MySQL, MS SQL Server, and PostgreSQL, are coded in C (the first three of them actually both in C and C++).

Databases are used in all kind of systems: financial, government, media, entertainment, telecommunications, health, education, retail, social networks, web, and the like.

Databases Powered by C
3D Movies
3D movies are created with applications that are generally written in C and C++. Those applications need to be very efficient and fast, since they handle a huge amount of data and do many calculations per second. The more efficient they are, the less time it takes for the artists and animators to generate the movie shots, and the more money the company saves.

Embedded Systems
Imagine that you wake up one day and go shopping. The alarm clock that wakes you up is likely programmed in C. Then you use your microwave or coffee maker to make your breakfast. They are also embedded systems and therefore are probably programmed in C. You turn on your TV or radio while you eat your breakfast. Those are also embedded systems, powered by C. When you open your garage door with the remote control you are also using an embedded system that is most likely programmed in C.

Then you get into your car. If it has the following features, also programmed in C:

automatic transmission
tire pressure detection systems
sensors (oxygen, temperature, oil level, etc.)
memory for seats and mirror settings.
dashboard display
anti-lock brakes
automatic stability control
cruise control
climate control
child-proof locks
keyless entry
heated seats
airbag control
You get to the store, park your car and go to a vending machine to get a soda. What language did they use to program this vending machine? Probably C. Then you buy something at the store. The cash register is also programmed in C. And when you pay with your credit card? You guessed it: the credit card reader is, again, likely programmed in C.

All those devices are embedded systems. They are like small computers that have a microcontroller/microprocessor inside that is running a program, also called firmware, on embedded devices. That program must detect key presses and act accordingly, and also display information to the user. For example, the alarm clock must interact with the user, detecting what button the user is pressing and, sometimes, how long it is being pressed, and program the device accordingly, all while displaying to the user the relevant information. The anti-lock brake system of the car, for example, must be able to detect sudden locking of the tires and act to release the pressure on the brakes for a small period of time, unlocking them, and thereby preventing uncontrolled skidding. All those calculations are done by a programmed embedded system.

Although the programming language used on embedded systems can vary from brand to brand, they are most commonly programmed in the C language, due to the language’s features of flexibility, efficiency, performance, and closeness to the hardware.

Embedded Systems are Often Written in C
Why is the C Programming Language Still Used?
There are many programming languages, today, that allow developers to be more productive than with C for different kinds of projects. There are higher level languages that provide much larger built-in libraries that simplify working with JSON, XML, UI, web pages, client requests, database connections, media manipulation, and so on.

But despite that, there are plenty of reasons to believe that C programming will remain active for a long time.

In programming languages one size does not fit all. Here are some reasons that C is unbeatable, and almost mandatory, for certain applications.

Portability and Efficiency
C is almost a portable assembly language. It is as close to the machine as possible while it is almost universally available for existing processor architectures. There is at least one C compiler for almost every existent architecture. And nowadays, because of highly optimized binaries generated by modern compilers, it’s not an easy task to improve on their output with hand written assembly.

Such is its portability and efficiency that “compilers, libraries, and interpreters of other programming languages are often implemented in C”. Interpreted languages like Python, Ruby, and PHP have their primary implementations written in C. It is even used by compilers for other languages to communicate with the machine. For example, C is the intermediate language underlying Eiffel and Forth. This means that, instead of generating machine code for every architecture to be supported, compilers for those languages just generate intermediate C code, and the C compiler handles the machine code generation.
