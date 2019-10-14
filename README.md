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

## Http & Https
<img src="https://sun9-34.userapi.com/c850732/v850732340/1eac21/-jNBiT-cHjk.jpg">
<img src="https://sun9-38.userapi.com/c855636/v855636175/129108/JJCB2RXO5O4.jpg">
<img src="https://sun9-62.userapi.com/c855636/v855636175/129111/waIGbNdC3x0.jpg">
<img src="https://sun9-21.userapi.com/c851132/v851132292/1dfc14/_AlQM_0YgKo.jpg">

Q: Name at least three possible negative consequences of not using https  
A: 1. Losing private data.  
   2. Out site could be blocked by webbrowser.
   3. Possible losing of costumers.
Q: Explain the main idea behind public key cryptography in few sentences  
A: Public key cryptography need for safety transport messages in Internet. There is symmetry and asymmetry key. In case of symmetry key message will encrypt by key and will be decrypt by same way. Assymetric key its when message was encrypted by one key and decrypted by another. 
Q: You are creating and application for pet clinic. You need to implement the following functionality:
 1. add new pet (including name, age, breed, owner's name, medical history)
 2. search pet by name
 3. change name of an existing pet
 4. add new info about pet's health
 5. assign a pet to a particular doctor in the clinic
 6. register an appointment for a pet. This request should include info about pet, doctor and appointment date and time.
A: -

