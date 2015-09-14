import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class control_schemes extends PApplet {

/**
 * Control scheme testing software
 * Author: ADB
 */

// Some vars to initialize
IntDict downKeys;
String keys = "`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./ ~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?";

// Setup
public void setup(){
    size(500, 500);
    background(0);

    downKeys = new IntDict();
    for(int i = 0; i < keys.length(); i++){
        downKeys.set(str(keys.charAt(i)), PApplet.parseInt(false));
    }
    downKeys.set("up", PApplet.parseInt(false));
    downKeys.set("down", PApplet.parseInt(false));
    downKeys.set("left", PApplet.parseInt(false));
    downKeys.set("right", PApplet.parseInt(false));
}

// Char vars
float xPos = width/2;
float yPos = width/2;
float speed = 2;
float circumference = 30;

// Draw loop
public void draw(){
    // Draw over previous frame
    background(0);

    if(PApplet.parseBoolean(downKeys.get(" "))){
        stroke(255, 255, 255);
    }else{
        if(PApplet.parseBoolean(downKeys.get("w"))){
            yPos -= speed;
        }
        if(PApplet.parseBoolean(downKeys.get("s"))){
            yPos += speed;
        }
        if(PApplet.parseBoolean(downKeys.get("a"))){
            xPos -= speed;
        }
        if(PApplet.parseBoolean(downKeys.get("d"))){
            xPos += speed;
        }

        if(PApplet.parseBoolean(downKeys.get("up"))){
            fill(255, 0, 0);
            rect(xPos - circumference/2, yPos - circumference/2, circumference, 0-circumference);
        }
        if(PApplet.parseBoolean(downKeys.get("down"))){
            fill(255, 0, 0);
            rect(xPos - circumference/2, yPos + circumference/2, circumference, circumference);
        }
        if(PApplet.parseBoolean(downKeys.get("left"))){
            fill(255, 0, 0);
            rect(xPos - circumference/2, yPos - circumference/2, 0-circumference, circumference);
        }
        if(PApplet.parseBoolean(downKeys.get("right"))){
            fill(255, 0, 0);
            rect(xPos + circumference/2, yPos - circumference/2, circumference, circumference);
        }
        noStroke();
    }
    fill(255, 0, 0);
    ellipse(xPos, yPos, circumference, circumference);
}


public void keyPressed(){
    if(key != CODED){
        downKeys.set(str(key), PApplet.parseInt(true));
    }else{
        switch(keyCode){
            case UP:
                downKeys.set("up", PApplet.parseInt(true));
                break;
            case DOWN:
                downKeys.set("down", PApplet.parseInt(true));
                break;
            case LEFT:
                downKeys.set("left", PApplet.parseInt(true));
                break;
            case RIGHT:
                downKeys.set("right", PApplet.parseInt(true));
                break;
            default:
                break;
        }
    }
}
public void keyReleased(){
    if(key != CODED){
        downKeys.set(str(key), PApplet.parseInt(false));
    }else{
        switch(keyCode){
            case UP:
                downKeys.set("up", PApplet.parseInt(false));
                break;
            case DOWN:
                downKeys.set("down", PApplet.parseInt(false));
                break;
            case LEFT:
                downKeys.set("left", PApplet.parseInt(false));
                break;
            case RIGHT:
                downKeys.set("right", PApplet.parseInt(false));
                break;
            default:
                break;
        }
    }
}
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "--full-screen", "--bgcolor=#666666", "--stop-color=#cccccc", "control_schemes" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
