int LDR = 0; 
int buzzer = 5; 
int val = 0; 
int result = 5; 
float debut, fin, tempsEcoule; 
boolean finCode = true; 

void setup() { 
 	pinMode(LDR, INPUT); 
 	Serial.begin(9600); 
} 

void loop() { 
 	val = analogRead(LDR); 

 	if (val < 800){ 
 		finCode = false; 
 		debut = millis(); 
 		tone(buzzer,1000); 

 		while(val < 800){ 
 			fin = millis(); 
 			tempsEcoule = fin-debut; 

 			if(tempsEcoule<500){ 
 				result = 0; 
 			} else if((tempsEcoule>500)&&(tempsEcoule<=1500)){ 
 			result = 1; 
 			} else if(tempsEcoule>1500) 
 				result = 2; 

 			val = analogRead(LDR); 
 		} noTone(buzzer); 

 		Serial.print(result); 
 		debut = millis(); 

 		while((val >= 800)&&(!finCode)){ 
	  	val = analogRead(LDR); 
 			fin = millis(); 
 			tempsEcoule = fin - debut; 

 			if(tempsEcoule >= 1000){ 
 				result = 3; 
 				finCode==true; 
 				Serial.print(result); 
 				break; 
 			} 
 		} 
 	} 
}
