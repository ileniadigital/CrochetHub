<template>
  <div>
    <!-- Action button -->
    <button class="btn btn-primary" type="button" data-bs-toggle="modal" data-bs-target="#editModal">
      <i class="bi bi-pencil-square"></i>
    </button>

    <!-- Modal -->
    <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="editModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="editModalLabel">Edit {{ modelName }}</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <!-- Pass model-specific fields to ActionForm -->
            <ActionForm ref="actionForm" :data="data" @submit="formSubmit" />
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" @click="saveChanges">Save changes</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ActionForm from './ActionForm.vue';
const url = 'http://localhost:8000';

export default {
  data() {
    return {
      data: {
        type: Object,
        required: true,
      }
    };
  },
  components: { 
    ActionForm },
  props: {
    data: {
      type: Object,
      required: true,
    },
  },
  methods: {
    async saveChanges() {
      // Call the submitForm method of the ActionForm component
      this.$refs.actionForm.submitForm();
    },
    formSubmit(formData) {
      // Now you have the form data to send in the PUT request
      this.submitYarnData(formData);
    },
    async submitYarnData(formData) {
      console.log('Form data:', formData);
      try {
        const yarnId = formData.id; // Get the ID from the passed data
        if (!yarnId) {
          console.error('Yarn ID is missing in the data:', this.data);
          return;
        }
        console.log('Yarn ID:', yarnId);
        console.log(`${url}/api/yarns/${yarnId}`);
        const response = await axios.put(`${url}/api/yarn/${yarnId}`, formData); 
        console.log('Item edited', response.data); 
      } catch (error) {
        console.error('Error during PUT request:', error);
      }
    }
  }
};
</script>
