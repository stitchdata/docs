    - name: _type
      type: ['null', string]
      description: <WRITE ME>
    - name: attachments
      type: array
      decription: <WRITE ME>
      array-properties:
      - name: content_id
        type: ['null', string]
        description: <WRITE ME>
      - name: content_type
        type: ['null', string]
        description: <WRITE ME>
      - name: filename
        type: ['null', string]
        description: <WRITE ME>
      - name: size
        type: ['null', integer]
        description: <WRITE ME>
      - name: url
        type: ['null', string]
        description: <WRITE ME>
    - name: bcc
      type: array
      decription: <WRITE ME>
      array-properties: ['null', string]
    - name: body_html
      type: ['null', string]
      description: <WRITE ME>
    - name: body_html_quoted
      type: array
      decription: <WRITE ME>
      array-properties:
      - name: expand
        type: ['null', integer, boolean]
        description: <WRITE ME>
      - name: html
        type: ['null', string]
        description: <WRITE ME>
    - name: body_preview
      type: ['null', string]
      description: <WRITE ME>
    - name: body_text
      type: ['null', string]
      description: <WRITE ME>
    - name: body_text_quoted
      type: array
      decription: <WRITE ME>
      array-properties:
      - name: expand
        type: ['null', integer, boolean]
        description: <WRITE ME>
      - name: text
        type: ['null', string]
        description: <WRITE ME>
    - name: cc
      type: array
      decription: <WRITE ME>
      array-properties: ['null', string]
    - name: contact_id
      type: ['null', string]
      description: <WRITE ME>
    - name: created_by
      type: ['null', string]
      description: <WRITE ME>
    - name: created_by_name
      type: ['null', string]
      description: <WRITE ME>
    - name: date_created
      type: ['null', string]
      description: <WRITE ME>
    - name: date_scheduled
      type: ['null', string]
      description: <WRITE ME>
    - name: date_sent
      type: ['null', string]
      description: <WRITE ME>
    - name: date_updated
      type: ['null', string]
      description: <WRITE ME>
    - name: dialer_id
      type: ['null', string]
      description: <WRITE ME>
    - name: direction
      type: ['null', string]
      description: <WRITE ME>
    - name: duration
      type: ['null', integer]
      description: <WRITE ME>
    - name: email_account_id
      type: ['null', string]
      description: <WRITE ME>
    - name: envelope
      type: object
      description: <WRITE ME>
      object-properties:
      - name: bcc
        type: array
        decription: <WRITE ME>
        array-properties:
        - name: email
          type: ['null', string]
          description: <WRITE ME>
        - name: name
          type: ['null', string]
          description: <WRITE ME>
      - name: cc
        type: array
        decription: <WRITE ME>
        array-properties:
        - name: email
          type: ['null', string]
          description: <WRITE ME>
        - name: name
          type: ['null', string]
          description: <WRITE ME>
      - {name: date, type: null, description: <WRITE ME>}
      - name: from
        type: array
        decription: <WRITE ME>
        array-properties:
        - name: email
          type: ['null', string]
          description: <WRITE ME>
        - name: name
          type: ['null', string]
          description: <WRITE ME>
      - name: in_reply_to
        type: ['null', string]
        description: <WRITE ME>
      - name: is_autoreply
        type: ['null', integer, boolean]
        description: <WRITE ME>
      - name: message_id
        type: ['null', string]
        description: <WRITE ME>
      - name: reply_to
        type: array
        decription: <WRITE ME>
        array-properties:
        - name: email
          type: ['null', string]
          description: <WRITE ME>
        - name: name
          type: ['null', string]
          description: <WRITE ME>
      - name: sender
        type: array
        decription: <WRITE ME>
        array-properties:
        - name: email
          type: ['null', string]
          description: <WRITE ME>
        - name: name
          type: ['null', string]
          description: <WRITE ME>
      - name: subject
        type: ['null', string]
        description: <WRITE ME>
      - name: to
        type: array
        decription: <WRITE ME>
        array-properties:
        - name: email
          type: ['null', string]
          description: <WRITE ME>
        - name: name
          type: ['null', string]
          description: <WRITE ME>
    - name: id
      type: ['null', string]
      description: <WRITE ME>
    - name: import_id
      type: ['null', string]
      description: <WRITE ME>
    - name: in_reply_to_id
      type: ['null', string]
      description: <WRITE ME>
    - name: lead_id
      type: ['null', string]
      description: <WRITE ME>
    - name: local_phone
      type: ['null', string]
      description: <WRITE ME>
    - name: message_ids
      type: array
      decription: <WRITE ME>
      array-properties: ['null', string]
    - name: need_smtp_credentials
      type: ['null', integer, boolean]
      description: <WRITE ME>
    - name: new_status_id
      type: ['null', string]
      description: <WRITE ME>
    - name: new_status_label
      type: ['null', string]
      description: <WRITE ME>
    - name: new_status_type
      type: ['null', string]
      description: <WRITE ME>
    - name: note
      type: ['null', string]
      description: <WRITE ME>
    - name: old_status_id
      type: ['null', string]
      description: <WRITE ME>
    - name: old_status_label
      type: ['null', string]
      description: <WRITE ME>
    - name: old_status_type
      type: ['null', string]
      description: <WRITE ME>
    - name: opens
      type: array
      decription: <WRITE ME>
      array-properties:
      - name: ip_address
        type: ['null', string]
        description: <WRITE ME>
      - name: opened_at
        type: ['null', string]
        description: <WRITE ME>
      - name: opened_by
        type: ['null', string]
        description: <WRITE ME>
      - name: user_agent
        type: ['null', string]
        description: <WRITE ME>
    - name: opens_summary
      type: ['null', string]
      description: <WRITE ME>
    - name: opportunity_confidence
      type: ['null', integer]
      description: <WRITE ME>
    - name: opportunity_date_won
      type: ['null', string]
      description: <WRITE ME>
    - name: opportunity_id
      type: ['null', string]
      description: <WRITE ME>
    - name: opportunity_value
      type: ['null', integer]
      description: <WRITE ME>
    - name: opportunity_value_currency
      type: ['null', string]
      description: <WRITE ME>
    - name: opportunity_value_formatted
      type: ['null', string]
      description: <WRITE ME>
    - name: opportunity_value_period
      type: ['null', string]
      description: <WRITE ME>
    - name: organization_id
      type: ['null', string]
      description: <WRITE ME>
    - name: phone
      type: ['null', string]
      description: <WRITE ME>
    - name: recording_url
      type: ['null', string]
      description: <WRITE ME>
    - name: references
      type: array
      decription: <WRITE ME>
      array-properties: ['null', string]
    - name: remote_phone
      type: ['null', string]
      description: <WRITE ME>
    - name: send_attempts
      type: array
      decription: <WRITE ME>
      array-properties:
      - name: date
        type: ['null', string]
        description: <WRITE ME>
      - name: error_class
        type: ['null', string]
        description: <WRITE ME>
      - name: error_message
        type: ['null', string]
        description: <WRITE ME>
    - name: sender
      type: ['null', string]
      description: <WRITE ME>
    - name: source
      type: ['null', string]
      description: <WRITE ME>
    - name: status
      type: ['null', string]
      description: <WRITE ME>
    - name: subject
      type: ['null', string]
      description: <WRITE ME>
    - name: task_assigned_to
      type: ['null', string]
      description: <WRITE ME>
    - name: task_assigned_to_name
      type: ['null', string]
      description: <WRITE ME>
    - name: task_id
      type: ['null', string]
      description: <WRITE ME>
    - name: task_text
      type: ['null', string]
      description: <WRITE ME>
    - name: template_id
      type: ['null', string]
      description: <WRITE ME>
    - name: template_name
      type: ['null', string]
      description: <WRITE ME>
    - name: thread_id
      type: ['null', string]
      description: <WRITE ME>
    - name: to
      type: array
      decription: <WRITE ME>
      array-properties: ['null', string]
    - name: transferred_from
      type: ['null', string]
      description: <WRITE ME>
    - name: transferred_to
      type: ['null', string]
      description: <WRITE ME>
    - name: updated_by
      type: ['null', string]
      description: <WRITE ME>
    - name: updated_by_name
      type: ['null', string]
      description: <WRITE ME>
    - name: user_id
      type: ['null', string]
      description: <WRITE ME>
    - name: user_name
      type: ['null', string]
      description: <WRITE ME>
    - name: users
      type: array
      decription: <WRITE ME>
      array-properties: []
    - name: voicemail_duration
      type: ['null', integer]
      description: <WRITE ME>
    - name: voicemail_url
      type: ['null', string]
      description: <WRITE ME>
    