# Perceptron Model

1. **Initialization:**

   - Weights \( w_1, w_2, w_0 \) (including bias) are initialized to zero.
   - Learning rate (\( \eta \)) is set.
   - Number of epochs (iterations) is set.

   ![Initialization](https://i.imgur.com/ztvAzgx.png)

2. **Inputs and Weights:**

   - Inputs \( x_1 \) and \( x_2 \) are provided.
   - Bias \( x_0 \) is set to 1.

   ![Inputs and Weights](https://i.imgur.com/3oj0q9z.png)

3. **Weighted Sum Calculation:**

   - Compute the weighted sum \( z \) using the formula:
     \[
     z = w_0 \cdot x_0 + w_1 \cdot x_1 + w_2 \cdot x_2
     \]

   ![Weighted Sum Calculation](https://i.imgur.com/PJ7nW4K.png)

4. **Activation Function:**

   - Apply the step function (activation function) to the weighted sum \( z \):
     \[
     \text{output} = \begin{cases} 
      1 & \text{if } z \geq 0 \\
      0 & \text{if } z < 0 
     \end{cases}
     \]

   ![Activation Function](https://i.imgur.com/Uci5DQ2.png)

5. **Training Process:**

   - For each epoch, iterate through all training samples:
     - Compute the predicted output.
     - Update the weights based on the error using the formula:
       \[
       w_i \leftarrow w_i + \eta \cdot (\text{target} - \text{prediction}) \cdot x_i
       \]

   ![Training Process](https://i.imgur.com/ERvW6PM.png)

6. **Training Example:**

   - Let's go through one epoch with an example:

     ![Training Example](https://i.imgur.com/EApJLyD.png)

     - Assume initial weights \( w_0 = 0, w_1 = 0, w_2 = 0 \).
     - Learning rate \( \eta = 0.01 \).

     **Step-by-Step Training:**
     1. For input \( [0, 0] \) with target 0:
        - \( z = 0 \cdot 1 + 0 \cdot 0 + 0 \cdot 0 = 0 \)
        - Prediction = 1 (since \( z \geq 0 \))
        - Error = 0 - 1 = -1
        - Update weights:
          \[
          w_0 \leftarrow 0 + 0.01 \cdot (-1) \cdot 1 = -0.01
          \]
          \[
          w_1 \leftarrow 0 + 0.01 \cdot (-1) \cdot 0 = 0
          \]
          \[
          w_2 \leftarrow 0 + 0.01 \cdot (-1) \cdot 0 = 0
          \]

     2. For input \( [0, 1] \) with target 0:
        - \( z = -0.01 \cdot 1 + 0 \cdot 0 + 0 \cdot 1 = -0.01 \)
        - Prediction = 0 (since \( z < 0 \))
        - Error = 0 - 0 = 0
        - No change in weights.

     3. For input \( [1, 0] \) with target 0:
        - \( z = -0.01 \cdot 1 + 0 \cdot 1 + 0 \cdot 0 = -0.01 \)
        - Prediction = 0 (since \( z < 0 \))
        - Error = 0 - 0 = 0
        - No change in weights.

     4. For input \( [1, 1] \) with target 1:
        - \( z = -0.01 \cdot 1 + 0 \cdot 1 + 0 \cdot 1 = -0.01 \)
        - Prediction = 0 (since \( z < 0 \))
        - Error = 1 - 0 = 1
        - Update weights:
          \[
          w_0 \leftarrow -0.01 + 0.01 \cdot 1 \cdot 1 = 0
          \]
          \[
          w_1 \leftarrow 0 + 0.01 \cdot 1 \cdot 1 = 0.01
          \]
          \[
          w_2 \leftarrow 0 + 0.01 \cdot 1 \cdot 1 = 0.01
          \]

     - After one epoch, the updated weights are \( w_0 = 0, w_1 = 0.01, w_2 = 0.01 \).

### Visualization

1. **Input Space and Decision Boundary:**

   - The perceptron adjusts its weights to learn a decision boundary that separates the classes.

2. **Epochs Progress:**

   - As the number of epochs increases, the decision boundary becomes better at separating the classes.

### Conclusion

This pictorial representation should help visualize the perceptron's functioning, including initialization, weighted sum calculation, activation, and the training process with weight updates. By iteratively adjusting the weights, the perceptron learns to classify the input data correctly.
