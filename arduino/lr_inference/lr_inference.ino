# include "arduino_model_params.h"

// int freeMemory() {
//   extern int __heap_start, *__brkval;
//   int v;
//   return (int)&v - (__brkval == 0 ? (int)&__heap_start : (int)__brkval);
// }

void scale_raw_sample(float raw[], float scaled[]){

  for(int i=0; i < N_FEATURES; i++){
    scaled[i]= (raw[i] - Scaler_mean[i])/ Scaler_scale[i];
  }
}

int predict_lr(float x[]){
  float z= Intercept;

  for(int i= 0; i < N_FEATURES; i++){
    z+= Coefficients[i] * x[i];
  }

  if (z > 0){
    return 1;
  }
  else{
    return 0;
  }

}

int predict_dt(float x[]){


  if (x[0] <= 0.73) {

      if (x[3] <= -1.04)
          return 0;
      else
          return 1;

  } 
  else {

      if (x[0] <= 0.90) {

          if (x[2] <= 0.02)
              return 1;
          else
              return 0;

      } 
      else {
          return 0;
      }
  }

}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  delay(2000);

  float sample[N_FEATURES]= {0.2, -1.0, 0.6, 0.2, -1.3};
  float scaled[N_FEATURES];

  scale_raw_sample(sample, scaled);

  // Serial.print("Free RAM before ..: ");
  // Serial.println(freeMemory());

  unsigned long start_lr= micros();
  int prediction_lr= predict_lr(scaled);

  unsigned long end_lr= micros();
  
  
  unsigned long start_dt= micros();
  int prediction_dt= predict_dt(scaled);

  unsigned long end_dt= micros();
  
  // Serial.print("Free RAM after ..T: ");
  // Serial.println(freeMemory());

// Printing to Serial Monitor

  Serial.print("LR Prediction: ");
  Serial.println(prediction_lr);

  Serial.print("LR Inference time (microseconds): ");
  Serial.println(end_lr - start_lr);


  Serial.print("DT Prediction: ");
  Serial.println(prediction_dt);

  Serial.print("DT Inference time (microseconds): ");
  Serial.println(end_dt - start_dt);

}

void loop() {

  // stays empty since we run inference only once in this project
}
