<template>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css">
    <!-- Action button -->
    <button :class="buttonClass" type="button" :data-bs-toggle="'modal'" :data-bs-target="`#${action}Modal`">
      <i :class="iconClass"></i>
    </button>
    
    <!-- Modal -->
    <div class="modal fade" :id="`${action}Modal`" tabindex="-1" :aria-labelledby="`${action}ModalLabel`" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" :id="`${action}ModalLabel`">{{ modalTitle }}</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            This is a modal to {{ action }} a yarn.
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button type="button" :class="footerButtonClass">{{ footerButtonText }}</button>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      action: {
        type: String,
        required: true
      }
    },
    computed: {
      buttonClass() {
        console.log('Button Class:', this.action === 'edit' ? 'btn btn-primary' : 'btn btn-danger');
        return this.action === 'edit' ? 'btn btn-primary' : 'btn btn-danger';
      },
      iconClass() {
        console.log('Icon Class:', this.action === 'edit' ? 'bi bi-pencil-square' : 'bi bi-trash-fill');
        return this.action === 'edit' ? 'bi bi-pencil-square' : 'bi bi-trash-fill';
      },
      modalTitle() {
        console.log('Modal Title:', this.action.charAt(0).toUpperCase() + this.action.slice(1));
        return this.action.charAt(0).toUpperCase() + this.action.slice(1);
      },
      footerButtonClass() {
        console.log('Footer Button Class:', this.action === 'edit' ? 'btn btn-primary' : 'btn btn-danger');
        return this.action === 'edit' ? 'btn btn-primary' : 'btn btn-danger';
      },
      footerButtonText() {
        console.log('Footer Button Text:', this.action === 'edit' ? 'Save changes' : 'Delete');
        return this.action === 'edit' ? 'Save changes' : 'Delete';
      }
    },
    mounted() {
      console.log('Component Mounted:', this.action);
      console.log(document.querySelector(`#${this.action}Modal`)); // Debugging statement
    }
  };
  </script>
  