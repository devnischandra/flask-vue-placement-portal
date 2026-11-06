<template>
    <button :type="type" :disabled="disabled" @click="$emit('click')" :class="`btn btn-${btnClass}`">{{ label }}</button>
</template>

<script>
export default{
    props: ['type','btnClass', 'label', 'disabled'],
    emits: ['click']
}
</script>
