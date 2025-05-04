<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Chat History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <MobileHeader/>
      <div id="ivhhhh-2" class="middle-content">
        <div class="form-section shadow-border">
          <h3>Employee Information</h3>
          <div class="form-grid">
            <div class="form-group">
              <label for="employee-name">Employee Name</label>
              <input type="text" id="employee-name" value="Nguyễn Văn A" readonly="" class="readonly-link"/>
            </div>
            <div class="form-group">
              <label for="position">Position</label>
              <input type="text" id="position" value="Software Engineer" readonly=""/>
            </div>
            <div class="form-group">
              <label for="department-3">Department</label> <!-- Changed id -->
              <input type="text" id="department-3" value="IT" readonly=""/>
            </div>
            <div class="form-group">
              <label for="review-period">Review Period</label>
              <input type="text" id="review-period" value="Q2 2025" readonly=""/>
            </div>
          </div>
          <button type="button" class="ai-button"><i class="fa-solid fa-wand-magic-sparkles"></i> Assess with AI</button>
        </div>
        <div class="form-section shadow-border">
          <h3>Performance Data</h3>
          <div class="placeholder-ai-output" id="i86thbg">
            Placeholder for displaying relevant KPIs, goals, and work results from ERPNext (e.g., project completion rates, sales targets met, etc.). Could include small charts or tables.
          </div>
        </div>
        <div class="form-section shadow-border">
          <h3>Assessment Criteria</h3>
          <!-- Criteria 1: Productivity -->
          <div class="form-grid">
            <div class="form-group">
              <label>Criteria: Productivity</label>
            </div>
            <div class="form-group">
              <label>AI Assessment</label>
              <div class="ai-suggestion-area">
                <p><strong>Rating:</strong> 4/5 (Exceeds Expectations)</p>
                <p><strong>Justification:</strong> Consistently completed tasks ahead of schedule. High output on Project Phoenix.</p>
              </div>
            </div>
            <div class="form-group">
              <label for="manual-rating-productivity">Manual Rating</label>
              <select type="text" id="manual-rating-productivity">
                <option>Select Rating...</option>
                <option value="1">1 - Needs Improvement</option>
                <option value="2">2 - Meets Expectations</option>
                <option value="3">3 - Good</option>
                <option value="4" selected>4 - Exceeds Expectations</option>
                <option value="5">5 - Outstanding</option>
              </select>
            </div>
            <div id="ilsg1mi-2" class="form-group"> <!-- Span 2 -->
              <label for="manual-comments-productivity">Manual Comments</label>
              <textarea id="manual-comments-productivity" rows="2" placeholder="Enter your assessment comments..."></textarea>
            </div>
          </div>
          <hr id="icuo6xk"/>
          <!-- Criteria 2: Quality -->
          <div class="form-grid">
            <div class="form-group">
              <label>Criteria: Quality of Work</label>
            </div>
            <div class="form-group">
              <label>AI Assessment</label>
              <div class="ai-suggestion-area">
                <p><strong>Rating:</strong> 3/5 (Good)</p>
                <p><strong>Justification:</strong> Code quality generally good, minor bugs reported in initial submissions, quickly fixed.</p>
              </div>
            </div>
            <div class="form-group">
              <label for="manual-rating-quality">Manual Rating</label>
              <select type="text" id="manual-rating-quality">
                <option>Select Rating...</option>
                <option value="1">1 - Needs Improvement</option>
                <option value="2">2 - Meets Expectations</option>
                <option value="3" selected>3 - Good</option>
                <option value="4">4 - Exceeds Expectations</option>
                <option value="5">5 - Outstanding</option>
              </select>
            </div>
            <div id="ikpvu21-2" class="form-group"> <!-- Span 2 -->
              <label for="manual-comments-quality">Manual Comments</label>
              <textarea id="manual-comments-quality" rows="2" placeholder="Enter your assessment comments..."></textarea>
            </div>
          </div>
          <hr id="iwijbij"/>
          <!-- Add more criteria sections as needed -->
        </div>
        <div class="form-section shadow-border">
          <h3>Overall Summary &amp; Development Plan</h3>
          <div class="form-grid">
            <div id="i35kh6-2" class="form-group"> <!-- Spans 2 columns -->
              <label for="overall-comments">Overall Comments</label>
              <textarea id="overall-comments" rows="4" placeholder="Enter overall feedback..."></textarea>
            </div>
            <div id="i0p5l9-2" class="form-group"> <!-- Spans 2 columns -->
              <label for="development-plan">Development Plan / Training Suggestions</label>
              <textarea id="development-plan" rows="4" placeholder="Outline areas for growth or training..."></textarea>
            </div>
          </div>
          <div class="form-actions">
            <button type="button" class="secondary">Save Draft</button>
            <button type="button" class="success">Confirm &amp; Save</button>
            <button type="button" class="info">Send Result Notification</button>
            <button type="button" class="danger">Cancel</button>
          </div>
        </div>
      </div> <!-- End middle-content -->
      <!-- Bottom Navigation (Optional or adjust as needed) -->
      <!-- <div class="bottom-nav"> ... </div> -->
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