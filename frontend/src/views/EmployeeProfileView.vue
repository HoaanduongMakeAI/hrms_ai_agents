<template>
  <div class="main-container gjs-grid-row">
    <!-- Left Column (Chat History) -->
    <ChatHistorySection />

    <!-- Middle Column (Workspace) -->
    <div class="middle-column gjs-grid-column">
      <MobileHeader/>
      <div class="middle-content"> <!-- Scroll wrapper -->
        <h1>HR Management</h1>
        <h2 id="irjfpq">Employee Profile (Add/Edit)</h2>
        <!-- Employee Form -->
        <div class="employee-form">
          <!-- CV Upload Section -->
          <div id="ifk5bh" class="form-section cv-upload-section gjs-grid-row">
            <h4><i class="fa-solid fa-file-upload"></i> Import from CV (UC-01, FR-18)</h4>
            <div class="form-group gjs-grid-column">
              <label for="cv-file">Upload CV (.pdf, .docx)</label>
              <input type="file" id="cv-file" name="cv-file"/>
            </div>
            <div class="status gjs-grid-column">
              <i class="fa-solid fa-info-circle"></i> Status: Ready / Processing... / Extracted.
            </div>
            <div class="extracted-data gjs-grid-column">
              <strong>Extracted Data (Placeholder):</strong><br/>
              - Full Name: Nguyễn Văn A<br/>
              - Email: a@example.com<br/>
              - Phone: 090xxxxxxx<br/>
              - Experience: 3 years at XYZ Corp (Developer)...<br/><em>(Comparison view shown here if updating - UC-01 2.A1.3)</em>
            </div>
            <div class="cv-actions gjs-grid-column">
              <button type="button" class="primary"><i class="fa-solid fa-check"></i> Apply CV Data</button>
              <button type="button" class="secondary"><i class="fa-solid fa-times"></i> Cancel CV</button>
            </div>
          </div>
          <!-- Basic Information -->
          <div class="form-section shadow-border">
            <h3><i class="fa-solid fa-user"></i> Basic Information</h3>
            <div class="form-grid gjs-grid-row">
              <div class="form-group gjs-grid-column">
                <label for="employee_number">Employee Number</label>
                <input type="text" id="employee_number" name="employee_number" value="EMP/0001" class="shadow-border"/>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="employee_id">Employee ID (ERPNext User)</label>
                <input type="text" id="employee_id" name="employee_id" value="nguyenvana@company.com" readonly=""/>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="first_name">First Name</label>
                <input type="text" id="first_name" name="first_name" value="Văn" class="shadow-border"/>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="middle_name">Middle Name</label>
                <input type="text" id="middle_name" name="middle_name" value="" class="shadow-border"/>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="last_name">Last Name</label>
                <input type="text" id="last_name" name="last_name" value="Nguyễn" class="shadow-border"/>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="employee_name">Full Name (Readonly)</label>
                <input type="text" id="employee_name" name="employee_name" value="Nguyễn Văn A" readonly=""/>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="date_of_birth">Date of Birth</label>
                <input type="date" id="date_of_birth" name="date_of_birth" class="shadow-border"/>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="gender">Gender</label>
                <select type="text" id="gender" name="gender" class="shadow-border">
                  <option>Male</option>
                  <option>Female</option>
                  <option>Other</option>
                </select>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="avatar">Image</label>
                <input type="file" id="avatar" name="avatar"/>
                <div class="image-placeholder"><i class="fa-solid fa-image"></i> Avatar</div>
              </div>
            </div>
          </div>
          <!-- Contact Information -->
          <div class="form-section shadow-border">
            <h3><i class="fa-solid fa-address-book"></i> Contact Information</h3>
            <div class="form-grid gjs-grid-row">
              <div class="form-group gjs-grid-column">
                <label for="cell_number">Mobile Number</label>
                <input type="tel" id="cell_number" name="cell_number" class="shadow-border"/>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="personal_email">Personal Email</label>
                <input type="email" id="personal_email" name="personal_email" class="shadow-border"/>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="company_email">Company Email</label>
                <input type="email" id="company_email" name="company_email" class="shadow-border"/>
              </div>
              <div id="i35kh6" class="form-group gjs-grid-column"> <!-- Span across columns -->
                <label for="current_address">Current Address</label>
                <textarea id="current_address" name="current_address" class="shadow-border"></textarea>
              </div>
              <div id="i0p5l9" class="form-group gjs-grid-column">
                <label for="permanent_address">Permanent Address</label>
                <textarea id="permanent_address" name="permanent_address" class="shadow-border"></textarea>
              </div>
            </div>
          </div>
          <!-- Job Information -->
          <div class="form-section shadow-border">
            <h3><i class="fa-solid fa-briefcase"></i> Job Information</h3>
            <div class="form-grid gjs-grid-row">
              <div class="form-group gjs-grid-column">
                <label for="company">Company</label>
                <select type="text" id="company" name="company" class="shadow-border">
                  <option>Main Company</option>
                </select>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="designation">Designation</label>
                <select type="text" id="designation" name="designation" class="shadow-border">
                  <option>Developer</option>
                  <option>Tester</option>
                </select>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="department">Department</label>
                <select type="text" id="department" name="department" class="shadow-border">
                  <option>IT</option>
                  <option>Sales</option>
                </select>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="date_of_joining">Date of Joining</label>
                <input type="date" id="date_of_joining" name="date_of_joining" class="shadow-border"/>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="contract_end_date">Contract End Date</label>
                <input type="date" id="contract_end_date" name="contract_end_date" class="shadow-border"/>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="status">Status</label>
                <select type="text" id="status" name="status" class="shadow-border">
                  <option>Active</option>
                  <option>Inactive</option>
                  <option>Left</option>
                </select>
              </div>
              <div class="form-group gjs-grid-column">
                <label for="reports_to">Reports To</label>
                <select type="text" id="reports_to" name="reports_to" class="shadow-border">
                  <option>Trần Văn D (Manager)</option>
                </select>
              </div>
            </div>
          </div>
          <!-- Salary & Benefits (Placeholder) -->
          <div class="form-section shadow-border">
            <h3><i class="fa-solid fa-dollar-sign"></i> Salary &amp; Benefits (UC-13)</h3>
            <div class="placeholder">Placeholder for Salary &amp; Benefits fields (May be restricted)</div>
          </div>
          <!-- Leave Information (Placeholder) -->
          <div class="form-section shadow-border">
            <h3><i class="fa-solid fa-calendar-alt"></i> Leave Information (UC-13)</h3>
            <div class="placeholder">Leave Balance: 10 days (Read-only)</div>
          </div>
          <!-- Education & Experience (Placeholder) -->
          <div class="form-section shadow-border">
            <h3><i class="fa-solid fa-graduation-cap"></i> Education &amp; Experience</h3>
            <div class="child-table-placeholder shadow-border">Placeholder for Education Table (`education`)</div>
            <div id="i7hj7z" class="child-table-placeholder shadow-border">Placeholder for External Work History Table (`external_work_history`)</div>
          </div>
          <!-- Skills (Placeholder) -->
          <div class="form-section shadow-border">
            <h3><i class="fa-solid fa-cogs"></i> Skills</h3>
            <div class="placeholder">Placeholder for Skills (Tags or Child Table)</div>
          </div>
          <!-- Form Actions -->
          <div class="form-actions gjs-grid-row">
            <button type="button" class="danger"><i class="fa-solid fa-trash"></i> Delete</button>
            <button type="button" class="secondary"><i class="fa-solid fa-times"></i> Cancel</button>
            <button type="button" class="primary"><i class="fa-solid fa-save"></i> Save</button>
            <!-- <button class="primary"><i class="fas fa-check-circle"></i> Confirm Save (from Chat)</button> -->
          </div>
        </div>
      </div> <!-- End middle-content -->
      <!-- Bottom Navigation -->
      <div class="bottom-nav">
        <button type="button" class="active">All Employees</button> <!-- Should be active if navigating from list -->
        <button type="button">Departments</button>
        <button type="button">Positions</button>
      </div>
    </div>

    <!-- Right Column (Tabs) -->
    <TabSection />
  </div>
</template>

<script setup>
import ChatHistorySection from '../components/ChatHistorySection.vue';
import TabSection from '../components/TabSection.vue';

// Component logic goes here if needed
</script>