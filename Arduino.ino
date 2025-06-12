bool iniciado = false;

void setup() {
  pinMode(11, OUTPUT);
  Serial.begin(9600);  // Inicia la comunicación serial
  while (!Serial) {
    ; // Espera a que el puerto serial esté listo (para placas como Leonardo)
  }
}

void loop() {
  // Escuchar comandos seriales desde la PC
  if (Serial.available()) {
    String comando = Serial.readStringUntil('\n');  // Leer hasta nueva línea
    comando.trim();  // Elimina espacios en blanco o saltos de línea

    if (comando == "START") {
      iniciado = true;
      Serial.println("Recibido: START");
    } else if (comando == "STOP") {
      iniciado = false;
      digitalWrite(11, LOW);  // Asegurar que el pin quede apagado
      Serial.println("Recibido: STOP");
    }
  }

  // Si fue iniciado, ejecutar el parpadeo
  if (iniciado) {
    digitalWrite(11, HIGH);
    delay(1000);
    digitalWrite(11, LOW);
    delay(1000);
  }
}
