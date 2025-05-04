<template>
  <div id="i5od9-3" class="main-container gjs-grid-row">
    <!-- Left Column (Chat History Alt) -->
    <ChatHistorySectionAlt />

    <!-- Middle Column (Chat Section) -->
    <div id="ieme5" class="gjs-grid-column">
      <MobileHeader />
      <div id="ido8e1" class="gjs-grid-row">
        <div id="imwyil" class="gjs-grid-column">
          <button type="button" id="i6y6kk">Action 1</button>
        </div>
        <div id="inqlb5" class="gjs-grid-column">
          <button type="button" id="iupih2">Action 1</button>
        </div>
      </div>
      <!-- Input Area Section -->
      <div id="ijlkw5" class="gjs-grid-row">
        <div id="i41n78" class="gjs-grid-column">
          <h1 id="ifm4i"><span id="ik3yy">Welcome back</span></h1>
          <div id="i9115" class="gjs-grid-row">
            <div id="i41td" class="gjs-grid-column">
              <textarea id="i53dr"></textarea>
              <!-- Input Area Buttons Section -->
              <div id="input-area-buttons-row-2" class="gjs-grid-row">
                <div id="input-area-actions-col-2" class="gjs-grid-column">
                  <button type="button" class="light-button">Action 1</button>
                  <button type="button" class="light-button">Attach File</button>
                </div>
                <div id="input-area-send-button-col-2" class="gjs-grid-column">
                  <img src="../assets/send_svgrepo_com.svg" id="iyb2zy"/>
                </div>
              </div>
            </div>
          </div>
          <div id="i9zt5l" class="gjs-grid-row">
            <div id="i730jb" class="gjs-grid-column">
              <button type="button" id="iul597" class="button-light">Action 1</button>
              <button type="button" id="ibtpvh">Action 1</button>
            </div>
          </div>
        </div>
      </div>
      <div id="ido8e1-2-3-2" class="gjs-grid-row">
        <div id="imwyil-2-3-2" class="gjs-grid-column">
          <img id="i8j5k5-2-2" src="../assets/menu_svgrepo_com__2_.svg"/>
          <h1 id="i2cdk-2-2-2-2">AI Agent</h1>
        </div>
      </div>
    </div>

    <!-- Right Column (Tabs) -->
    <TabSection />
  </div>
</template>

<script setup>
import ChatHistorySectionAlt from '../components/ChatHistorySectionAlt.vue';
import MobileHeader from '../components/MobileHeader.vue';
import TabSection from '../components/TabSection.vue';

// Component logic goes here if needed
</script>