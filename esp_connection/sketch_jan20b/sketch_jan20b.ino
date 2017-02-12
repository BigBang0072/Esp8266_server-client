#include <SoftwareSerial.h>
const int delay_time=1000;

SoftwareSerial wifi_module(10, 11); // RX, TX

void setup() 
{
  Serial.begin(115200);
  wifi_module.begin(115200);
  
  // Testing the wifi_module is responding or not
  Serial.println("Testing the wifi_module:");
  delay(delay_time);
  wifi_module.println("AT");
  delay(delay_time);
  if (compare_response("OK"))
  {
    Serial.println("Device Found");
  }
  else
  {
    Serial.println(wifi_module.readString());
    Serial.println("Device not found");
    //while(1);                                           //stopping any furthur code to execute.
  }
  delay(delay_time);

  //RESET the wifi_module
  wifi_module.println("AT+RST");
  delay(delay_time);
  
  //Turn the echo OFF (WHY???)
  wifi_module.println("ATE0");
  delay(delay_time);
  if (compare_response("OK"))
  {
    Serial.println("ECHO off");
  } 

  // Creating server on the Wifi_module
  wifi_module.println("AT+CWMODE=3");
  delay(delay_time);
  if (compare_response("OK"))
  {
    Serial.println("Mode changed to both server and client mode");
  }
  wifi_module.println("AT+CIPMUX=1");
  delay(delay_time);
  wifi_module.println("AT+CIPSERVER=1,8080");
  delay(delay_time);
  if (compare_response("OK"))
  {
    Serial.println("Server created on port 8080");
  }
  delay(delay_time);
}
int i=100;
void loop() 
{
  if(wifi_module.find("+IPD"))
  {
   Serial.println("Got the Connection");
   wifi_module.println("AT+CIPSEND=0,3");
   delay(25);
   wifi_module.println(i);
   i=i+1;
  }
}


int compare_response(char response[])
{
  if (wifi_module.available())
  {
    if (wifi_module.find(response))
    {
      return 1;
    }
    else
    {
      return 0;
    }
  }
}

