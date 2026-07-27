<template>
    <button :type="button" @click="$emit('click')" :class="`btn btn-${btnType}`">{{ label }}</button>
</template>

<script>
export default{
    props: ['btnType', 'label'],
    emits: ['click']
}
</script>