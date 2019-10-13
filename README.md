# kottans-backend
 I had never work with GitHub so it was a new experience for me
 Main problem i faced with was: "How to set Pycharm as text editor in Github Desktop?"
 But after hour of suffering i finally came through it =)

#Unix Shell

<img src="https://camo.githubusercontent.com/d15521ce009a66b0edf648bc51b0c7795da56b4d/68747470733a2f2f73756e392d32312e757365726170692e636f6d2f633835303532382f763835303532383331382f3162383832382f4337762d567a526753754d2e6a7067">
<img src="https://sun9-54.userapi.com/c850728/v850728320/1de760/ubtl884FJ-0.jpg">

## Memory Management

Q: What's going to happen if program reaches maximum limit of stack ?  
A: We have stack overflow and the program receives a Segmentation Fault.  
Q: What's going to happen if program requests a big (more then 128KB) memory allocation on heap ?  
A: The heap is enlarged via the brk() system call to make room for the requested block.  
Q: What's the difference between Text and Data memory segments ?  
A: Data memory segments able to read and write.
Memory address lives in the data segments.
Text memory segments read-only and executing.
Text segments also maps binary file in memory, but writes to this are will lead to Segmentation Fault.
<img src="https://sun9-60.userapi.com/c854028/v854028086/1210d8/xay7XqUytB4.jpg">

About lesson: I've done theoretical part of this lesson, but practical was to difficult to do.
First, `ps -a`, `/proc/<PID>/maps` did not work. Basing on material I googled,
I think it's because this commands for Linux and I am using Windows, so i tried to do everything i could.

## TCP. UDP. Network

<img src="https://sun9-46.userapi.com/c850736/v850736931/1ee3d7/jafrIbE_Be4.jpg">

About lesson: It was very interesing to figure out how Internet works and what problems i could face and solve them as future web developer. However, practice part i didnt :( .
