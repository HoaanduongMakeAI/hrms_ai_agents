<template>
  <div id="id4sxml-2-2-4" class="left-column gjs-grid-column">
    <div id="iqd6k-3-2-3-2-11-2-2-4" class="gjs-grid-row">
      <div id="iiz7h-3-2-3-2-11-2-2-4" class="gjs-grid-column">
        <h1 id="i2cdk-2-3-2-11-2-2-4">AI Agent</h1>
      </div>
      <div id="iq22g-2-3-2-11-2-2-4" class="gjs-grid-column">
        <img src="../assets/menu_svgrepo_com__1_.svg" id="i64tdrx"/> <!-- Updated path -->
      </div>
    </div>
    <button type="button" id="i6m5mt-2-3-2-11-2-2-4" class="chat-history-button">New Chat</button>
    <!-- History Toggle Button -->
    <button type="button" id="history-toggle-button" title="Collapse History" @click="toggleHistory" ref="historyToggleButtonRef">
      <i id="i32cl1p" class="fas fa-chevron-up" ref="toggleIconRef"></i> <!-- Start with 'up' icon -->
    </button>
    <!-- Chat History Scroll Area -->
    <div id="i3uvw-3-2-2-6-2-2-4" class="gjs-grid-column chat-history-scroll-area" ref="historyScrollAreaRef">
      <div id="ijq67-4-2-2-6-2-2-4" class="gjs-grid-row">
        <!-- Chat History Group -->
        <div id="izo3pi-5-2-2-6-2-2-4" class="gjs-grid-column chat-history-group-column">
          <div id="ivwzi8-5-2-2-6-2-2-4" class="chat-history-group-title"><b id="i6rtns-5-2-2-6-2-2-4">Today</b></div>
          <!--  -->
          <div id="izzxb7-6-2-2-6-2-2-4" class="gjs-grid-row chat-history-item-row">
            <div id="iaykcx-6-2-2-6-2-2-4" class="gjs-grid-column chat-history-item-col-1">
              <div id="i6719g-6-2-2-6-2-2-4" class="chat-history-item-title">rtyuidvjanenjenrkjlqnrlkqjwenqweqweqwewqe</div>
            </div>
            <div id="i2r02b-6-2-2-6-2-2-4" class="gjs-grid-column chat-history-item-col-2">
              <img src="../assets/options_svgrepo_com.svg" class="chat-history-item-option" id="i3ds6tq"/> <!-- Updated path -->
            </div>
          </div>
          <div id="izzxb7-2-6-2-2-6-2-2-4" class="gjs-grid-row chat-history-item-row">
            <div id="iaykcx-2-6-2-2-6-2-2-4" class="gjs-grid-column chat-history-item-col-1">
              <div id="i6719g-2-6-2-2-6-2-2-4" class="chat-history-item-title">rtyuidvjanenjenrkjlqnrlkqjwenqweqweqwewqe</div>
            </div>
            <div id="i2r02b-2-6-2-2-6-2-2-4" class="gjs-grid-column chat-history-item-col-2">
              <img src="../assets/options_svgrepo_com.svg" class="chat-history-item-option" id="i9ymup8"/> <!-- Updated path -->
            </div>
          </div>
          <div id="izzxb7-2-2-5-2-2-6-2-2-4" class="gjs-grid-row chat-history-item-row">
            <div id="iaykcx-2-2-5-2-2-6-2-2-4" class="gjs-grid-column chat-history-item-col-1">
              <div id="i6719g-2-2-5-2-2-6-2-2-4" class="chat-history-item-title">rtyuidvjanenjenrkjlqnrlkqjwenqweqweqwewqe</div>
            </div>
            <div id="i2r02b-2-2-5-2-2-6-2-2-4" class="gjs-grid-column chat-history-item-col-2">
              <img src="../assets/options_svgrepo_com.svg" class="chat-history-item-option" id="iqkajej"/> <!-- Updated path -->
            </div>
          </div>
          <!--  -->
        </div>
      </div>
      <div id="ijq67-2-3-2-2-6-2-2-4" class="gjs-grid-row">
        <!-- Chat History Group -->
        <div id="izo3pi-3-3-2-2-6-2-2-4" class="gjs-grid-column chat-history-group-column">
          <div id="ivwzi8-3-3-2-2-6-2-2-4" class="chat-history-group-title"><b id="i6rtns-3-3-2-2-6-2-2-4">Yesterday</b></div> <!-- Changed title -->
          <!--  -->
          <div id="izzxb7-4-3-2-2-6-2-2-4" class="gjs-grid-row chat-history-item-row">
            <div id="iaykcx-4-3-2-2-6-2-2-4" class="gjs-grid-column chat-history-item-col-1">
              <div id="i6719g-4-3-2-2-6-2-2-4" class="chat-history-item-title">rtyuidvjanenjenrkjlqnrlkqjwenqweqweqwewqe</div>
            </div>
            <div id="i2r02b-4-3-2-2-6-2-2-4" class="gjs-grid-column chat-history-item-col-2">
              <img src="../assets/options_svgrepo_com.svg" class="chat-history-item-option" id="itapgba"/> <!-- Updated path -->
            </div>
          </div>
          <div id="izzxb7-2-4-3-2-2-6-2-2-4" class="gjs-grid-row chat-history-item-row">
            <div id="iaykcx-2-4-3-2-2-6-2-2-4" class="gjs-grid-column chat-history-item-col-1">
              <div id="i6719g-2-4-3-2-2-6-2-2-4" class="chat-history-item-title">rtyuidvjanenjenrkjlqnrlkqjwenqweqweqwewqe</div>
            </div>
            <div id="i2r02b-2-4-3-2-2-6-2-2-4" class="gjs-grid-column chat-history-item-col-2">
              <img src="../assets/options_svgrepo_com.svg" class="chat-history-item-option" id="i2ikmr5"/> <!-- Updated path -->
            </div>
          </div>
          <div id="izzxb7-2-2-3-3-2-2-6-2-2-4" class="gjs-grid-row chat-history-item-row">
            <div id="iaykcx-2-2-3-3-2-2-6-2-2-4" class="gjs-grid-column chat-history-item-col-1">
              <div id="i6719g-2-2-3-3-2-2-6-2-2-4" class="chat-history-item-title">rtyuidvjanenjenrkjlqnrlkqjwenqweqweqwewqe</div>
            </div>
            <div id="i2r02b-2-2-3-3-2-2-6-2-2-4" class="gjs-grid-column chat-history-item-col-2">
              <img src="../assets/options_svgrepo_com.svg" class="chat-history-item-option" id="ilc43hr"/> <!-- Updated path -->
            </div>
          </div>
          <!--  -->
        </div>
      </div>
    </div> <!-- End chat-history-scroll-area -->
    <!-- Collapsed History View (Tabs & Sample Convo) -->
    <div id="isisdtf" class="collapsed-history-view" ref="collapsedHistoryViewRef">
      <ul id="iu4slah" class="conversation-tabs" ref="tabsContainerRef" @click="switchTab">
        <li data-tab="convo1" id="idcdl6e" class="tab-item active">Sample Convo 1</li>
        <li data-tab="convo2" id="i1odkiv" class="tab-item">Sample Convo 2</li>
        <!-- Add more tabs as needed -->
      </ul>
      <div id="ipsernb" class="tab-content-area" ref="panesContainerRef">
        <div id="convo1-2-4" class="tab-content-pane active">
          <!-- Sample Conversation 1 -->
          <div id="i4vnufr" class="sample-message user"><div id="ichwkh4" class="bubble">Tell me about the performance review criteria for developers.</div></div>
          <div id="i31m8zp" class="sample-message ai"><div id="i4tcclg" class="bubble">Certainly. Key criteria include Code Quality, Timeliness, Collaboration, Problem Solving, and adherence to Best Practices. Would you like details on any specific criterion?</div></div>
          <div id="i72q74g" class="sample-message user"><div id="iwkvpui" class="bubble">Yes, tell me more about Code Quality.</div></div>
          <div id="imtxetn" class="sample-message ai"><div id="ipk2y0h" class="bubble">Code Quality is assessed based on readability, efficiency, maintainability, test coverage, and minimizing bugs. We look for clean, well-documented, and robust code.</div></div>
          <!-- End Sample Convo 1 -->
        </div>
        <div id="convo2-2-4" class="tab-content-pane">
          <!-- Sample Conversation 2 -->
          <div id="iuhyju5" class="sample-message user"><div id="ivwjyvl" class="bubble">What's the status of leave request #123?</div></div>
          <div id="ihzp3yk" class="sample-message ai"><div id="is0hs9f" class="bubble">Leave request #123 submitted by John Doe is currently pending manager approval.</div></div>
          <!-- End Sample Convo 2 -->
        </div>
        <!-- Add more panes corresponding to tabs -->
      </div>
    </div>
    <!-- Original Bottom Chat Input Area -->
    <div id="iinnvcj-2-2-4" class="chat-input-area gjs-grid-column">
      <div id="ish7dzb-2-2-4" class="gjs-grid-row">
        <textarea placeholder="Type your message..." id="i7usdom-2-2-4"></textarea>
      </div>
      <div id="ixhi6h8-2-2-4" class="gjs-grid-row">
        <div id="iut30rf-2-2-4" class="input-buttons-left">
          <button type="button" title="Attach File" id="iu9t9qd-2-2-4" class="attach-button">
            <i id="i5yawgf-2-2-4" class="fa-solid fa-paperclip"></i>
          </button>
          <!-- Add other left buttons here if needed -->
        </div>
        <div id="ilpfgxk-2-2-4" class="input-buttons-right">
          <button type="button" title="Send Message" id="ivdjq7g-2-2-4" class="send-button">
            <i id="ivyh3gh-2-2-4" class="fa-solid fa-paper-plane"></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

// Refs for DOM elements
const historyToggleButtonRef = ref(null);
const historyScrollAreaRef = ref(null);
const collapsedHistoryViewRef = ref(null);
const toggleIconRef = ref(null);
const tabsContainerRef = ref(null);
const panesContainerRef = ref(null);

// --- History Toggle Logic ---
const toggleHistory = () => {
  const historyToggleButton = historyToggleButtonRef.value;
  const historyScrollArea = historyScrollAreaRef.value;
  const collapsedHistoryView = collapsedHistoryViewRef.value;
  const toggleIcon = toggleIconRef.value;

  if (historyToggleButton && historyScrollArea && collapsedHistoryView && toggleIcon) {
    const isCollapsed = historyScrollArea.classList.toggle('history-collapsed');
    collapsedHistoryView.classList.toggle('visible', isCollapsed);

    // Change icon and title based on collapsed state
    if (isCollapsed) {
      toggleIcon.classList.remove('fa-chevron-up');
      toggleIcon.classList.add('fa-chevron-down');
      historyToggleButton.title = "Expand History";
    } else {
      toggleIcon.classList.remove('fa-chevron-down');
      toggleIcon.classList.add('fa-chevron-up');
      historyToggleButton.title = "Collapse History";
    }
  } else {
    console.error("Could not find all required elements for history toggle:",
      { historyToggleButton, historyScrollArea, collapsedHistoryView, toggleIcon });
  }
};

// --- Tab Switching Logic ---
const switchTab = (event) => {
  const tabsContainer = tabsContainerRef.value;
  const panesContainer = panesContainerRef.value;

  if (tabsContainer && panesContainer && event.target.classList.contains('tab-item')) {
    const targetTabId = event.target.getAttribute('data-tab');

    // Deactivate all tabs and panes
    tabsContainer.querySelectorAll('.tab-item').forEach(tab => tab.classList.remove('active'));
    panesContainer.querySelectorAll('.tab-content-pane').forEach(pane => pane.classList.remove('active'));

    // Activate clicked tab and corresponding pane
    event.target.classList.add('active');
    // Note: Querying by ID within the component's scope might be tricky.
    // Consider using a different attribute or structure if this doesn't work reliably.
    // For now, we assume IDs are unique within the rendered component instance.
    const targetPane = panesContainer.querySelector(`#${targetTabId}-2-4`); // Adjusted ID based on original HTML
    if (targetPane) {
      targetPane.classList.add('active');
    } else {
      console.error(`Could not find tab pane with ID: ${targetTabId}-2-4`);
    }
  }
};

// onMounted(() => {
//   // Event listeners are attached via @click in the template now
//   // Initialization logic could go here if needed
// });

</script>
