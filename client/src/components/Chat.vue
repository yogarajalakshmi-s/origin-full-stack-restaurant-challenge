<template>
    <Dialog v-model="dialogVisible" header="Chat" :modal="false" class="chat-container">
        <div class="chat-messages">
            <div v-for="(message, index) in messages" :key="index" class="message">
                <div :class="{ 'user-message': message.isCustomer, 'employee-message': !message.isCustomer }">{{ message.text }}</div>
            </div>
            <input v-model="newMessage" @keyup.enter="sendMessage" class="chat-input" placeholder="Type your message..." />
        </div>
    </Dialog>
</template>

<script>

import Dialog from 'primevue/dialog';

export default {
  data() {
    return {
      dialogVisible: false,
      messages: [],
      newMessage: '',
      orderMessages: [
        "Welcome!",
        "Please tell us your preferred dish.",
        "Any specific customization?",
        "Please specify the quantity.",
        "Anything else you'd like to add?",
        "Please provide your delivery address.",
        "Thank you for the information.",
        "Your order has been placed. Estimated delivery time is 30 minutes.",
        "Enjoy your meal!",
        "Thank you for choosing our service. Have a great day!"
      ],
    };
  },

  components: {
    Dialog,
  },

  methods: {

    updateDialogVisibility(value) {
      this.dialogVisible = value;
    },

    sendMessage() {
        const userMessage = this.newMessage;

        // Pushing user message
        if (userMessage) {
            this.messages.push({ text: userMessage, isCustomer: true });
        }

        // Pushing employee message with a delay of 1.5 seconds
        const randomIndex = Math.floor(Math.random() * this.orderMessages.length);
        setTimeout(() => {
        this.messages.push({ text: this.orderMessages[randomIndex], isCustomer: false });
        }, 1500);

        this.newMessage = '';
    }
  },
};
</script>

<style scoped>

.chat-messages {
  max-height: 300px;
  overflow-y: auto;
}

.message {
  margin: 5px 0;
}

.user-message {
  text-align: right;
  background-color: #d3f4ed;
  padding: 5px;
  border-radius: 5px;
}

.employee-message {
  text-align: left;
  background-color: #f0f0f0;
  padding: 5px;
  border-radius: 5px;
}

.chat-input {
  width: 100%;
  padding: 5px;
  border: 1px solid #ccc;
}

.chat-container {
  position: fixed;
  right: 20px !important;
  bottom: 20px !important;
  transform: none !important;
  transition: transform 0.3s ease !important;
  z-index: 9999;
  max-width: 400px;
  width: 100%;
}


</style>
