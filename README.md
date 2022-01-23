# !&

Ever wanted to write code 4528x slower? Now you can!
This is a programming language solely built upon NAND gates.


# Syntax

This is how to define the initial conditions for updates, each slash shows a jump between frames.

    %input1,input2/input1,input2%

This is how you create objects.

    //: This is a comment!!! :
    !&: this is a nand gate, in1, in2, out1/out2 :
    <<: this is an input, out :
    >>: this is an output, in :

The `!&` (nand) object takes 4 arguments:
    
`name,
    input1,
    input2,
    output`

The `<<` (input) object takes 2 arguments:
    
`name,
    output`

The `>>` (output) object takes 2 arguments:
    
`name,
    input`

And the `//` (comment) object doesn't care.

-----

## by K01e