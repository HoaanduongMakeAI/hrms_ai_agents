<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Chat History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <MobileHeader/>
      <div id="ivhhhh-4" class="middle-content">
        <div class="form-section shadow-border">
          <h3>Request Details</h3>
          <div class="form-grid">
            <div class="form-group">
              <label for="employee-name-2">Employee Name</label>
              <input type="text" id="employee-name-2" value="Nguyễn Văn A" readonly="" class="readonly-link"/>
            </div>
            <div class="form-group">
              <label for="position-2">Position</label>
              <input type="text" id="position-2" value="Software Engineer" readonly=""/>
            </div>
            <div class="form-group">
              <label for="department-4">Department</label>
              <input type="text" id="department-4" value="IT" readonly=""/>
            </div>
            <div class="form-group">
              <label for="submission-date">Submission Date</label>
              <input type="date" id="submission-date" value="2025-04-28" readonly=""/>
            </div>
            <div class="form-group">
              <label for="requested-last-day">Requested Last Day</label>
              <input type="date" id="requested-last-day" value="2025-05-15" readonly=""/>
            </div>
            <div class="form-group">
              <label for="status-2">Current Status</label>
              <input type="text" id="status-2" value="Chờ duyệt" readonly=""/>
            </div>
            <div id="ihknx3-2" class="form-group">
              <label for="reason">Reason for Resignation</label>
              <textarea id="reason" rows="4" readonly="">Moving to another city for family reasons.</textarea>
            </div>
          </div>
        </div>
        <div class="form-section shadow-border">
          <h3>Supporting Information</h3>
          <div class="form-grid" id="iidwvcj">
            <div class="form-group">
              <label>Time with Company</label>
              <input type="text" value="3 years 2 months" readonly=""/>
            </div>
            <div class="form-group">
              <label>Performance History</label>
              <a href="#" class="form-link-display" id="i2trpk8">View Performance Reviews</a>
            </div>
            <div id="i35kh6-3" class="form-group">
              <label>AI Agent Context/Suggestions</label>
              <div class="placeholder-ai-output">
                - Employee is part of Project Phoenix (due end of May). Consider handover plan.<br/>
                - Company policy requires 15 working days notice (met).<br/>
                - No outstanding warnings or disciplinary actions.
              </div>
            </div>
          </div>
        </div>
        <div class="form-section shadow-border">
          <h3>Processing Actions</h3>
          <div class="form-grid">
            <div id="i0p5l9-3" class="form-group">
              <label for="notes">Rejection Reason / Notes</label>
              <textarea id="notes" rows="3" placeholder="Enter reason if rejecting, or optional notes if approving..."></textarea>
            </div>
          </div>
          <div class="form-actions">
            <button type="button" class="secondary">Request Clarification</button>
            <button type="button" class="danger">Reject</button>
            <button type="button" class="success">Approve</button>
            <button type="button" class="primary">Close</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Right Column (Tabs) -->
    <TabSection />
  </div>
</template>

<script setup>
import ChatHistorySection from '../components/ChatHistorySection.vue';
import MobileHeader from '../components/MobileHeader.vue';
import TabSection from '../components/TabSection.vue';

// Component logic goes here if needed
</script>