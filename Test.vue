<template>
    <v-container>
      <v-select
                  v-model="selectedOption"
                  :append-icon="selectedOption ? '' : 'mdi-check'"
                  autofocus
                  clearable
                  density="compact"
                  :error-messages="errorMessages"
                  :items="items"
                  variant="outlined"
                  :loading="loading"
                  label="Select an option"
                  @update:model-value="stopLoading"
              ></v-select>
  
              <v-btn variant="outlined" class="submit-button">
                  <v-icon>
                      mdi-check
                  </v-icon>
                  Submit
              </v-btn>
  
    </v-container>
    <router-view></router-view>
  </template>
  
  <script setup lang="ts">
  import { ref, reactive, computed, watch } from 'vue'
  const selectedOption = ref(null);
              const loading = ref(true); // Use ref for primitive values
              const errorMessages = ref('');
              const items = ref(['Option 1', 'Option 2', 'Option 3']);
  
              function stopLoading() {
                  loading.value = false; // Stop the loading indicator
              }
  
              function startLoading() {
                loading.value = true
              }
  
              watch(selectedOption, (newVal, oldVal) => {
                if(newVal !== null && oldVal === null) {
                  stopLoading()
                } else if (newVal === null && oldVal !== null) {
                  startLoading()
                }
              })
  
  
  </script>
  
  <style scoped>
   .v-select {
          width: 300px;
          max-height: 30px;
      }
      .submit-button {
          position: relative;
          left: 100px;
          top: 20px; /* Adjusted for better alignment */
          border: 1px solid black;
          width: 150px;
          height: 30px;
          display: flex;
          align-items: center;
          justify-content: center;
      }
  
  
  </style>
  