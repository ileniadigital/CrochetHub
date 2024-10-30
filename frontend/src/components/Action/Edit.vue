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
            <ActionForm :fields="fields" @submit="handleFormSubmit" />
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
import ActionForm from './ActionForm.vue';

export default {
  data() {
    return {
      fields: [
        { name: 'brand', label: 'Brand', type: 'text' },
        { name: 'material', label: 'Material', type: 'text' },
        { name: 'colour', label: 'Colour', type: 'text' },
        { name: 'weight', label: 'Weight', type: 'number' },
        { name: 'price', label: 'Price', type: 'number' },
        { name: 'yardage', label: 'Yardage', type: 'number' },
        { name: 'hookSize', label: 'Hook Size', type: 'number' }
    ],
    };
  },
  components: { 
    ActionForm },
  props: {
  },
  created() {
    console.log("Edit:", this.fields);
  },
  methods: {
    handleFormSubmit(formData) {
      console.log(`Form data for`, formData);
      // Process the form data (e.g., send it to an API or update local state)
    },
    saveChanges() {
      // Optionally trigger form submission here
    }
  }
};
</script>
