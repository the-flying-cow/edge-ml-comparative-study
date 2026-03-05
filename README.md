# Inferecing ML algorithm on Arduino Uno 3

# Objective
The objetive of ths project is to inference simple ML algorithms on Arduino Uno 3, and comparing their performance based on deployability and efficiency on these resource-constrained devices.

This project is a study of model selection under hardware constraints, and the trade-offs between model complexity and perforamce on embedded systems.

# Methodology
1. **Data Generation** : create a synthetic dataset with n samples and m features, suitable for classification or regression tasks.
2. **Model Selection** : choose a set of simple ML algorithms (e.g., Decision Trees, K-Nearest Neighbors, Logistic Regression) that can be implemented on Arduino Uno 3. (or any other device with similar constraints)
3. **Model Training** : train the selected models on the generated dataset using a suitable ML library (e.g., scikit-learn in Python).
4. **Export Parameters**: export the trained model parameters (e.g., weights, scaler) in a format that can be used for inference on Arduino.
5. **Setup Arduino**: set up the Arduino Uno 3 environment for inference, including necessary libraries and hardware configurations.
6. **Code on Arduino**: implement the inference code on Arduino, using the exported model parameters to make predictions based on new input data.
7. **Hardcoded Sample Test**: create a hardcoded sample input on the Arduino to test the inference code and verify the output against expected results.


# Performance Evaluation1
Evaluate the performance of each model based on:
- **Average Inference Time**: measure the average time taken for the Arduino to make a prediction using each model.
- **Average Memory Usage**: assess the average memory footprint of each model on the Arduino, including the size of the model parameters and the code.


# Conclusion
| Model               | Flash Usage    | SRAM Usage    | Inference Time |
| ------------------- | -------------- | ------------- | -------------- |
| Logistic Regression | **3444 bytes** | **344 bytes** | **92 µs**      |
| Decision Tree       | **3168 bytes** | **344 bytes** | **12 µs**      |

Based on the performance evaluation, the Decision Tree model demonstrates superior efficiency in terms of inference time and memory usage compared to Logistic Regression. The Decision Tree's lower flash usage along with its significantly faster inference time, makes it a more suitable choice for deployment on resource-constrained devices like the Arduino Uno 3. This is because Logistic Rergression requires compiled code for multiplication, loop operations and calculations, but Decision Trees only compile into branch instructions. Since, both models share the same feature, scaler and parameter arrays, SRAM usage is same for both models.

# OUtput Visuals
https://drive.google.com/drive/folders/18PJrPAi96iLW8x_JwXZXvK5xXz6VmfIP?usp=sharing