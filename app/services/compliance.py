import os
from typing import Dict

import openai
from fastapi import HTTPException

from app.client.openai import OpenAIClient


class Compliance:
    def __init__(self, compliance_policy: str):
        # URL of compliance policy
        self.compliance_policy = compliance_policy
        # URL of compliance policy
        self.compliance_policy = compliance_policy
        self.model = "gpt-4o-mini"
        self.max_token = 50
        self.OpenAI = OpenAIClient()

        # TODO : performance optimze
        # Approach for Caching Compliance Policy Data
        # Fetching and Caching Compliance Data:
        #
        # Initial Fetch: Fetch the compliance policy from the URL and store it in a cache (e.g., Redis).
        # Caching Strategy: Implement a mechanism to update the cached policy only if the policy has changed.
        # Change Detection:
        #
        # Hashing: Use a hashing algorithm (e.g., MD5,) to generate a hash of the compliance policy content.
        # Compare Hashes: Store the hash of the last fetched policy and compare it with the hash of the newly fetched policy to determine if there has been a change.
        # Cron Job for Regular Updates:
        #
        # Scheduled Fetch: Set up a cron job to periodically fetch the compliance policy from the URL.
        # Update Logic: Update the cache with the new policy only if the hash indicates that the policy has changed.

    def check_compliance(self, text: str):
        prompt = f"Check webpage content against the compliance policy: {self.compliance_policy}\n\nContent: {text}"
        try:

            completion = self.OpenAI.client.chat.completions.create(
              model=self.model,
              messages=[
                  {"role": "system", "content": "Check webpage content against the compliance policy"},
                  {"role": "user", "content": prompt}
              ]
            )

            return self.format_findings(completion.choices[0].message.content)

        except (openai.APIError, openai.APIConnectionError, openai.RateLimitError) as e:
            return f"Error communicating Performing compliance check Error : {e}"
        # all other error that are not part of openai.py error class like APIConnectionError , RateLimitError
        except Exception as e:
            print("IN this error", {e})
            raise HTTPException(status_code=500, detail=f"An unexpected error occurred during compliance checking: {e}")

    def format_findings(self, findings: str):

        sections = findings.split('\n\n')

        # Create a dictionary to store the results
        compliance_analysis = {}

        index = 1
        for section in sections:
            try:
                if section.startswith(f'{index}.'):
                    header, data = section[3:].strip().split(":")
                    compliance_analysis[header] = data
                    index = index + 1
            except Exception as e:
                compliance_analysis[index] = section
                index = index + 1

        return compliance_analysis

