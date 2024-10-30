<template>
  <form @submit.prevent="submitForm">
    <div v-for="field in fields" :key="field.name" class="mb-3">
      <label :for="field.name" class="form-label">{{ field.label }}</label>
      <input v-if="field.type === 'text'" type="text" :id="field.name" v-model="formData[field.name]" class="form-control" />
      <input v-else-if="field.type === 'number'" type="number" :id="field.name" v-model="formData[field.name]" class="form-control" />
      <textarea v-else-if="field.type === 'textarea'" :id="field.name" v-model="formData[field.name]" class="form-control"></textarea>
    </div>
  </form>
</template>

<script>
export default {
  props: {
    fields: {
      type: Array,
      required: true,
      default: () => []
    }
  },
  data() {
    return {
      formData: {}
    };
  },
  created() {
    // console.log("ActionForm fields:", this.fields);
    // // Initialize formData based on fields array
    // this.fields.forEach(field => {
    //   this.$set(this.formData, field.name, ''); // Initialize each field with an empty value
    // });
  },
  methods: {
    submitForm() {
      this.$emit('submit', this.formData); // Emit form data to parent component
    }
  }
};
</script>

<style>
    .mb-3 {
        display: flex;
        flex-direction: column;
        margin-bottom: 1em;
    }
    .form-label {
        text-align: left;
        margin-bottom: 0.5em;
        font-weight: bold;
    }
    .form-control {
        width: 100%;
        box-sizing: border-box;
    }
</style>