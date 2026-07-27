<template>
    <button :type="button" :class="`btn btn-${btnType}`">{{ label }}</button>
</template>

<script>
export default{
    props: ['btnType', 'label']
}
</script>