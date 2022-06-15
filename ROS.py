#!/usr/bin/env python3

import RPi.GPIO as GPIO
import curses
import time
import rospy
from time import sleep
from std_msgs.msg import String

pub=rospy.Publisher('talker',String,queue_size=20)
rospy.init_node('talker',anonymous=True)

en = 25
in1 = 23
in2 = 24
en1 = 17
in3 = 22
in4 = 27
temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)

GPIO.setup(en1,GPIO.OUT)
GPIO.setup(in1,GPIO.LOW)
GPIO.setup(in2,GPIO.LOW)
GPIO.setup(in3,GPIO.LOW)
GPIO.setup(in4,GPIO.LOW)

p1 = GPIO.PWM(en,1000)
p2 = GPIO.PWM(en1,1000)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p1.start(25)
p2.start(25)
w='working'
rospy.loginfo(w)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
GPIO.output(in2,GPIO.LOW)

def forward():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
def backward():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
def right():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
def left():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
def back_right():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
def back_left():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
def brake():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
try:
    while True:
        char = screen.getch()
        f='MOVING FORWARD'
        b='MOVING BACKWARD'
        r='TURNING RIGHT'
        l='TURNING LEFT'
        br='TURNING BACK RIGHT'
        bl='TURNING BACK LEFT'
        
        if char == ord('A'):
            A='RECIEVED LETTER A'
            rospy.loginfo(A)
            pub.publish(A)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1.5)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1.5)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1.5)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.75)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            backward()
            sleep(1.5)
            brake()
            sleep(0.5)
        if char == ord('B'):
            B="RECIEVED LETTER B"
            rospy.loginfo(B)
            pub.publish(B)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1.5)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.75)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.75)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(2)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(2)
            brake()
            sleep(0.5)
            rospy.loginfo(br)
            pub.publish(br)
            back_right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(2)
            brake()
            sleep(0.5)
            rospy.loginfo(br)
            pub.publish(br)
            back_right()
            sleep(2)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(2)
            brake()
            sleep(0.5)
        if char == ord('!'):
            GPIO.cleanup()
            break
        if char == ord('C'):
            C="RECIEVED LETTER C"
            rospy.loginfo(C)
            pub.publish(C)
            rospy.loginfo(b)
            pub.publish(f)
            backward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1.5)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1)
            brake()
            sleep(0.5)
        if char == ord('D'):
            D='RECIEVED LETTER D'
            rospy.loginfo(D)
            pub.publish(D)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1.5)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1.5)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
        if char == ord('E'):
            E='RECIEVED LETTER E'
            rospy.loginfo(E)
            pub.publish(E)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.75)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.6)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.6)
            brake()
            sleep(0.5)
            rospy.loginfo(l)
            pub.publish(l)
            left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.75)
            brake()
            sleep(0.5)
            rospy.loginfo(l)
            pub.publish(l)
            left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
        if char == ord('F'):
            F='RECIEVED LETTER F'
            rospy.loginfo(F)
            pub.publish(f)
            rospy.loginfo(l)
            pub.publish(l)
            left()
            sleep(1)#90
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.75)
            brake()
            sleep(0.5)
            rospy.loginfo(l)
            pub.publish(l)
            left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(l)
            pub.publish(l)
            left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.5)
            brake()
            sleep(0.5)
        if char == ord('G'):
            G='RECIEVED LETTER G'
            rospy.loginfo(G)
            pub.publish(G)
            rospy.loginfo(l)
            pub.publish(l)
            left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(l)
            pub.publish(l)
            left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(l)
            pub.publish(l)
            left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(l)
            pub.publish(l)
            left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(l)
            pub.publish(l)
            left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.5)
            brake()
            sleep(0.5)
        if char == ord('H'):
            H='RECIEVED LETTER H'
            rospy.loginfo(H)
            pub.publish(H)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
        if char == ord('I'):
            I='RECIEVED LETTER I'
            rospy.loginfo(I)
            pub.publish(I)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.25)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1)
            brake()
        if char == ord('J'):
            J='RECIEVED LETTER J'
            rospy.loginfo(J)
            pub.publish(J)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.4)
            brake()
            sleep()
        if char == ord('K'):
            K='RECIEVED LETTER K'
            rospy.loginfo(K)
            pub.publish(K)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.707)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.707)
            brake()
            sleep(0.5)
            rospy.loginfo(l)
            pub.publish(l)
            left()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.707)
            brake()
            sleep(0.5)
        if char == ord('L'):
            L='RECIEVED LETTER L'
            rospy.loginfo(L)
            pub.publish(L)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.5)
            brake()
            sleep(0.5)
        if char == ord('M'):
            M='RECIEVED LETTER M'
            rospy.loginfo(M)
            pub.publish(M)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.707)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.707)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1)
            brake()
            sleep(0.5)
        if char == ord('N'):
            N='RECIEVED LETTER N'
            rospy.loginfo(N)
            pub.publish(N)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1.414)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
        if char == ord('O'):
            O='RECIEVED LETTER O'
            rospy.loginfo(O)
            pub.publish(O)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()#90 degrees
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.60)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.60)
            brake()
            sleep(0.5)
        if char == ord('P'):
            P='RECIEVED LETTER P'
            rospy.loginfo(P)
            pub.publish(P)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.75)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.75)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.75)
            brake()
            sleep(0.5)
        if char == ord('Q'):
            Q='RECIEVED LETTER Q'
            rospy.loginfo(Q)
            pub.publish(Q)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()#90 degrees
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.75)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.75)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.75)
            brake()
            sleep(0.5)
            rospy.loginfo(br)
            pub.publish(br)
            back_right()
            sleep(0.5)#45 degrees
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.25)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.5)
            brake()
            sleep(0.5)
        if char == ord('R'):
            R='RECIEVED LETTER R'
            rospy.loginfo(R)
            pub.publish(R)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)#90 degrees
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(br)
            pub.publish(br)
            back_right()
            sleep(0.5)#45 degrees
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1.1)
            brake()
            sleep(0.5)
        if char == ord('S'):
            S='RECIEVED LETTER S'
            rospy.loginfo(S)
            pub.publish(S)
            rospy.loginfo(l)
            pub.publish(l)
            left()
            sleep(1)#90
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(l)
            pub.publish(l)
            left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(l)
            pub.publish(l)
            left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
        if char == ord('T'):
            T='RECIEVED LETTER T'
            rospy.loginfo(T)
            pub.publish(T)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)#90
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.35)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.35)
            brake()
            sleep(0.5)
        if char == ord('U'):
            U='RECIEVED LETTER U'
            rospy.loginfo(U)
            pub.publish(U)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)#90
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(l)
            pub.publish(l)
            left()
            sleep(1)#90
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
        if char == ord('V'):
            V='RECIEVED LETTER V'
            rospy.loginfo(V)
            pub.publish(V)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(0.5)#30 degrees
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1.11)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(f)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1.11)
            brake()
            sleep(0.5)
        if char == ord('W'):
            W='RECIEVED LETTER W'
            rospy.loginfo(W)
            pub.publish(W)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(0.5)#45
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.30)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.30)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
        if char == ord('X'):
            X='RECIEVED LETTER X'
            rospy.loginfo(X)
            pub.publish(X)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(1)#45
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1.414)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.707)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.707)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1.414)
            brake()
            sleep(0.5)
        if char == ord('Y'):
            Y='RECIEVED LETTER Y'
            rospy.loginfo(Y)
            pub.publish(Y)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(0.5)#45
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.707)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(0.707)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.707)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(0.75)
            brake()
            sleep(0.5)
        if char == ord('Z'):
            Z='RECIEVED LETTER Z'
            rospy.loginfo(Z)
            pub.publish(Z)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(1)#90
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
            rospy.loginfo(bl)
            pub.publish(bl)
            back_left()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(b)
            pub.publish(b)
            backward()
            sleep(1.414)
            brake()
            sleep(0.5)
            rospy.loginfo(r)
            pub.publish(r)
            right()
            sleep(0.5)
            brake()
            sleep(0.5)
            rospy.loginfo(f)
            pub.publish(f)
            forward()
            sleep(1)
            brake()
            sleep(0.5)
finally:
    curses.nocbreak();screen.keypad(0);curses.echo()
    curses.endwin()
    GPIO.cleanup()