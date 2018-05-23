
const int trigPin1 = 6;
const int echoPin1 = 7;

const int trigPin2 = 10;
const int echoPin2 = 9;

long duration;
int distanceCm, distanceInch;
const int MAX_DIST = 500; //cm
void setup() {
  
pinMode(trigPin1, OUTPUT);
pinMode(echoPin1, INPUT);

pinMode(trigPin2, OUTPUT);
pinMode(echoPin2, INPUT);
Serial.begin(9600);

}

void loop() {

int timeout = 500 * 2 /0.034; 

digitalWrite(trigPin1, LOW);
delayMicroseconds(2);
digitalWrite(trigPin1, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin1, LOW);
duration = pulseIn(echoPin1, HIGH, timeout);
distanceCm= duration*0.034/2;
distanceInch = duration*0.0133/2;
Serial.println(distanceCm);


digitalWrite(trigPin2, LOW);
delayMicroseconds(2);
digitalWrite(trigPin2, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin2, LOW);
duration = pulseIn(echoPin2, HIGH, timeout);
distanceCm= duration*0.034/2;
distanceInch = duration*0.0133/2;
Serial.println(distanceCm);
}
