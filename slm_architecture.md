                                Tensor 
                                  |                                          
                     ---------Autograd----------
                     |                         |
                    MSE                   Cross Entropy
                     |                         |       
                     |                         |
                     |                         |
                     ------Back propagation---------------------|
                                                                |
         MLP----------------------------------------------Linear layer----------------------------------------
          |                                                      |                   |                       |
          |                                                      |                   |                       |
    Hyperparameter turning       ---------------------RELU--------              Attention               Batch Norm
         |                      |                      |       \                    |                        |  
         |                      |                      |        \                   |                   Layer Norm
         |                      |                      |         \              Multi head Attention         |          
         |                      |                    Swish       GLU                                     RMS Norm
 mew scaling laws               |                      ----SwiGLU--                 -------------------------|
                                |                                                   |
                      Transformer block --------------------------------------------|                                      
                                |       
                                |
                           Transformer
                                |
                                |
                        Small language model                                       