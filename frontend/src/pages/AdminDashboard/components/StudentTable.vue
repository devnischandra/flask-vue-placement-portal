<template>
    <table class="table">
        <thead>
            <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Date of Birth</th>
                <th>Department</th>
                <th class="text-center">Action</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="student in students" :key="student.id">
                <td>{{ student.id }}</td>
                <td>{{ student.name }}</td>
                <td>{{ student.email }}</td>
                <td>{{ student.date_of_birth }}</td>
                <td>{{ student.department }}</td>
                <td class="text-center">
                    <BaseButton @click="$emit('update-user',student.id, {'is_blacklisted': true})" type="button" btn-class="primary" :label="student.is_blacklisted ? 'Unblock': 'Block' " />
                </td>
            </tr>
        </tbody>
    </table>
</template>

<script>
import BaseButton from '@/components/BaseButton.vue';

export default{
    components:{
        BaseButton
    },
    props: ["students"],
    emits:['update-user']
}
</script>