<template>
    <div class="mx-3 mt-3">
        <h4>Pending Companies</h4>
        <CompanyTable :companies="pendingCompanies"
        @update-company="$emit('update-company', ...arguments)"
        @update-user="$emit('update-user', ...arguments)"/>
    </div>
</template>

<script>
import CompanyTable from '../components/CompanyTable.vue';

export default {
    components:{
        CompanyTable
    },
    props: ["pendingCompanies"],
    emits:['update-company','update-user']
}
</script>