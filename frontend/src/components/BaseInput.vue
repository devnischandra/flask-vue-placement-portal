<template>
    <div class="mb-3">
        <label :for="id" class="form-label">{{ label }}</label>
        <input
            class="form-control"
            :type="type"
            :id="id"
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
        />
    </div>
</template>

<script>
export default{
    props: ['type','id','label','modelValue'],
    emits: ['update:modelValue']
}
</script>