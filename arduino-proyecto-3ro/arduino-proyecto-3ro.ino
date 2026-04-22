
#include <DHT.h>

#define DHT_PIN 2
#define DHT_PIN2 1
#define DHTTYPE DHT22
#define INDUCTIVE_PIN 3
#define SENSOR1 6
#define SENSOR2 7
#define SENSOR3 8

DHT dht(DHT_PIN, DHTTYPE);
DHT dht2(DHT_PIN2, DHT11);
void setup() {
  Serial.begin(9600);
  dht.begin();
  dht2.begin();
  pinMode(INDUCTIVE_PIN, INPUT);
  pinMode(SENSOR1, INPUT);
  pinMode(SENSOR2, INPUT);
  pinMode(SENSOR3, INPUT);
}

void loop() {
  Serial.println(digitalRead(SENSOR1));
  if (digitalRead(SENSOR1) == 0) {
    Serial.println("Inductivo");
    int inductivo = digitalRead(INDUCTIVE_PIN);
    if (inductivo) {
    Serial.println("metal");
    }
    else{
    Serial.println("no metal");

    }
  }
if (digitalRead(SENSOR2) == 0) {
    Serial.println("dht:");
    Serial.println("dht2:");

    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature();
    float humidity2 = dht2.readHumidity();
    float temperature2 = dht2.readTemperature();
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Error leyendo DHT22");
  } else {
    Serial.print("Humedad: ");
    Serial.print(humidity);
    Serial.print(" %  |  Temp: ");
    Serial.print(temperature);
    Serial.println(" C");

    Serial.print("Humedad Interna: ");
    Serial.print(humidity2);
    Serial.print(" %  |  Temp Interna: ");
    Serial.print(temperature2);
    Serial.println(" C");
  }
    }
if (digitalRead(SENSOR3) == 0) {
  Serial.println('SENSOR3');
  }
delay(50000000);
}