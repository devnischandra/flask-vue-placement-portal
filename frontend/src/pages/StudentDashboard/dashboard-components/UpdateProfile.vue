<template>
    <form @submit.prevent="$emit('update-profile', student)">
        <BaseInput type="text" id="email" label="Email" v-model="student.email" />
        <BaseInput type="number" id="cgpa" label="CGPA" v-model="student.cgpa" />
        <BaseInput type="url" id="resume_url" label="Resume URL" v-model="student.resume_url" />
        <BaseButton type="submit" btn-class="primary" label="Update" />
    </form>
</template>

<script>
import BaseButton from '@/components/BaseButton.vue';
import BaseInput from '@/components/BaseInput.vue';

export default{
    components:{
        BaseInput,
        BaseButton
    },
    props:["currentUser"],
    emits: ['update-profile'],
    data(){
        return {
            student:{
                email:this.currentUser.email,
                cgpa:this.currentUser.cgpa,
                resume_url:this.currentUser.resume_url
            }
        }
    }
}
</script>