<template>
    <div class="mx-3 mt-3">
        <h4>Registered Students</h4>
        <StudentTable :students="students"
        @update-user="(id, update) => $emit('update-user', id, update)"/>
    </div>
</template>

<script>
import StudentTable from '../components/StudentTable.vue';

export default {
    components:{
        StudentTable
    },
    props: ["students"],
    emits:['update-user']
}
</script>