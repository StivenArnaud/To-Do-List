<template>
    <div class="todo">
     <Todolist/>
    </div>
</template>

<script>
  import Todolist from '@/components/Todolist.vue';
  export default {
    name: 'Todo',
    components: {
      Todolist
    }
  }
</script>