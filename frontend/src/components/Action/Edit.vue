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
            <h1 class="modal-title fs-5" id="editModalLabel">Edit</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <!-- Pass fields to ActionForm -->
            <ActionForm ref="actionForm" :edit="true" :data="data" @submit="formSubmit" />
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary" @click="saveChanges" data-bs-dismiss="modal">Save
              changes</button>
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
      },
      edit: true,
    };
  },
  components: {
    ActionForm
  },
  props: {
    data: {
      type: Object,
      required: true,
    },
    model: {
      type: String,
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
      this.submitData(formData);
    },
    async submitData(formData) {
      try {
        if (!formData.id) {
          console.error('Yarn ID is missing in the data:', this.data);
          return;
        }

        const response = await axios.put(`${url}/api/${this.model}/${formData.id}/update`, formData);
        this.$emit('edited', response.data);
        console.log('Item edited', response.data);
      } catch (error) {
        console.error('Error during PUT request:', error);
      }
    }
  }
};
</script>
