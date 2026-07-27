<template>
    <button :type="type" @click="$emit('click')" :class="`btn btn-${btnClass}`">{{ label }}</button>
</template>

<script>
export default{
    props: ['type','btnClass', 'label'],
    emits: ['click']
}
</script>