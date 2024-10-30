<template>
    <form @submit.prevent="submitForm">
      <div v-for="(value, key) in data" :key="key" class="mb-3">
        <label :for="key" class="form-label">{{ key.charAt(0).toUpperCase() + key.slice(1) }}</label>
        <input
          v-if="typeof value === 'string'"
          type="text"
          :id="key"
          v-model="formData[key]"
          class="form-control"
        />
        <input
          v-else-if="typeof value === 'number'"
          type="number"
          :id="key"
          v-model="formData[key]"
          class="form-control"
        />
        <textarea
          v-else-if="typeof value === 'string' && value.length > 100"
          :id="key"
          v-model="formData[key]"
          class="form-control"
        ></textarea>
        <div v-else>
          <p>Unsupported field type for {{ key }}</p>
        </div>
      </div>
    </form>
  </template>
  
  <script>
  export default {
    props: {
      data: {
        type: Object,
        required: true,
        default: () => ({})
      }
    },
    data() {
      return {
        formData: {}
      };
    },
    created() {
      // Initialize formData from the data prop
      for (const key in this.data) {
        this.formData[key] = this.data[key] || '';
      }
    },
    methods: {
      submitForm() {
        this.$emit('submit', this.formData);
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