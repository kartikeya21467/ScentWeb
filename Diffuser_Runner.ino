int In1 = 7;
int In2 = 8;
int ENA = 5;
int SPEED = 255; // Maximum speed

void setup() {
  pinMode(In1, OUTPUT);
  pinMode(In2, OUTPUT);
  pinMode(ENA, OUTPUT);

  digitalWrite(In1, HIGH);
  digitalWrite(In2, LOW);
  analogWrite(ENA, 0);  // Initially stop the motor
  Serial.begin(9600);   // Start serial communication
}

void loop() {
  if (Serial.available() > 0) {
    char signal = Serial.read();
    // println("Signal received");
    if (signal == '1') {
      digitalWrite(In1, HIGH);
      digitalWrite(In2, LOW);
      analogWrite(ENA, SPEED);  // Run the motor for 10 seconds
      delay(10000);             // Delay for 10 seconds
      analogWrite(ENA, 0);      // Stop the motor
    }
  }
}
