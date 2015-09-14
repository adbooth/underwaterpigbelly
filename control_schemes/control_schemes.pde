/**
 * Control scheme testing software
 * Author: ADB
 */

// Some vars to initialize
IntDict downKeys;
String keys = "`1234567890-=qwertyuiop[]asdfghjkl;'zxcvbnm,./ ~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?";

// Setup
void setup(){
    size(500, 500);
    background(0);

    downKeys = new IntDict();
    for(int i = 0; i < keys.length(); i++){
        downKeys.set(str(keys.charAt(i)), int(false));
    }
    downKeys.set("up", int(false));
    downKeys.set("down", int(false));
    downKeys.set("left", int(false));
    downKeys.set("right", int(false));
}

// Char vars
float xPos = width/2;
float yPos = width/2;
float speed = 2;
float circumference = 30;

// Draw loop
void draw(){
    // Draw over previous frame
    background(0);

    if(boolean(downKeys.get(" "))){
        stroke(255, 255, 255);
    }else{
        if(boolean(downKeys.get("w"))){
            yPos -= speed;
        }
        if(boolean(downKeys.get("s"))){
            yPos += speed;
        }
        if(boolean(downKeys.get("a"))){
            xPos -= speed;
        }
        if(boolean(downKeys.get("d"))){
            xPos += speed;
        }

        if(boolean(downKeys.get("up"))){
            fill(255, 0, 0);
            rect(xPos - circumference/2, yPos - circumference/2, circumference, 0-circumference);
        }
        if(boolean(downKeys.get("down"))){
            fill(255, 0, 0);
            rect(xPos - circumference/2, yPos + circumference/2, circumference, circumference);
        }
        if(boolean(downKeys.get("left"))){
            fill(255, 0, 0);
            rect(xPos - circumference/2, yPos - circumference/2, 0-circumference, circumference);
        }
        if(boolean(downKeys.get("right"))){
            fill(255, 0, 0);
            rect(xPos + circumference/2, yPos - circumference/2, circumference, circumference);
        }
        noStroke();
    }
    fill(255, 0, 0);
    ellipse(xPos, yPos, circumference, circumference);
}


void keyPressed(){
    if(key != CODED){
        downKeys.set(str(key), int(true));
    }else{
        switch(keyCode){
            case UP:
                downKeys.set("up", int(true));
                break;
            case DOWN:
                downKeys.set("down", int(true));
                break;
            case LEFT:
                downKeys.set("left", int(true));
                break;
            case RIGHT:
                downKeys.set("right", int(true));
                break;
            default:
                break;
        }
    }
}
void keyReleased(){
    if(key != CODED){
        downKeys.set(str(key), int(false));
    }else{
        switch(keyCode){
            case UP:
                downKeys.set("up", int(false));
                break;
            case DOWN:
                downKeys.set("down", int(false));
                break;
            case LEFT:
                downKeys.set("left", int(false));
                break;
            case RIGHT:
                downKeys.set("right", int(false));
                break;
            default:
                break;
        }
    }
}
